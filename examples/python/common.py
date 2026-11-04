"""Call the hosted Actor once, inspect its summary, then read Dataset pages."""
import json
import os
from datetime import timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler, ProxyHandler
from apify_client import ApifyClient

ACTOR_ID = 'datascraperes/iherb-reviews-extractor'
ROOT = Path(__file__).resolve().parents[2]

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def credentials():
    token = os.environ.get('APIFY_API_TOKEN')
    if not token:
        raise RuntimeError('Set APIFY_API_TOKEN before calling the hosted Actor.')
    return token, os.environ.get('APIFY_API_BASE_URL', 'https://api.apify.com').rstrip('/')

def client():
    token, base = credentials()
    return ApifyClient(token, api_url=base, max_retries=2)

def start_once(actor_input, maximum_usd=0.01):
    token, base = credentials()
    query = urlencode({'timeout':240, 'maxTotalChargeUsd':maximum_usd})
    url = base+'/v2/acts/'+ACTOR_ID.replace('/', '~')+'/runs?'+query
    request = Request(url, data=json.dumps(actor_input).encode('utf-8'), method='POST',
                      headers={'Authorization':'Bearer '+token, 'Content-Type':'application/json'})
    # Start is intentionally sent once. Only SDK reads may retry.
    try:
        with build_opener(ProxyHandler({}), NoRedirect()).open(request, timeout=45) as response:
            run_id = json.load(response)['data']['id']
    except Exception:
        raise RuntimeError('Start failed or its response is unclear. Inspect recent runs in Apify Console before starting again.') from None
    print('Started run '+run_id, flush=True)
    return run_id

def wait_for_dataset(run_id):
    api = client()
    run = api.run(run_id).wait_for_finish(wait_duration=timedelta(seconds=270))
    status = getattr(run.status, 'value', run.status) if run else None
    if status != 'SUCCEEDED':
        raise RuntimeError('Run '+run_id+' did not succeed. Inspect it without starting another run.')
    record = api.key_value_store(run.default_key_value_store_id).get_record('RUN_SUMMARY')
    value = record['value'] if isinstance(record, dict) else record.value if record else None
    print('Dataset '+run.default_dataset_id, flush=True)
    if not isinstance(value,dict) or value.get('complete') is not True:
        raise RuntimeError('Collection incomplete or input needs correction. Inspect RUN_SUMMARY; saved rows remain accessible.')
    return run.default_dataset_id

def iter_rows(dataset_id, page_size=100):
    api = client()
    offset = 0
    while True:
        page = api.dataset(dataset_id).list_items(offset=offset, limit=page_size, clean=True)
        if not page.items:
            return
        yield from page.items
        offset += len(page.items)

def sample_input():
    return json.loads((ROOT/'data/sample-input.json').read_text(encoding='utf-8'))
