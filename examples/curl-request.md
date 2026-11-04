# Start one iHerb reviews request with cURL

From the repository root, set APIFY_API_TOKEN and run:

```bash
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary @data/sample-input.json \
  "https://api.apify.com/v2/acts/datascraperes~iherb-reviews-extractor/runs?timeout=240&maxTotalChargeUsd=0.01"
```

This asynchronous request returns a run ID. Do not automatically repeat a failed
or disconnected start: it may already have created a paid run. Inspect recent
runs in Console first. This command deliberately has no retry or redirect flag.

Use the returned ID for read-only polling:

```bash
curl --fail-with-body -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/actor-runs/$RUN_ID"
```

After SUCCEEDED, read RUN_SUMMARY from the returned defaultKeyValueStoreId:

```bash
curl --fail-with-body -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/key-value-stores/$STORE_ID/records/RUN_SUMMARY"
```

Require complete:true for a complete collection. Read individual review rows from the returned
defaultDatasetId, incrementing offset by the actual number received until empty:

```bash
curl --fail-with-body -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/datasets/$DATASET_ID/items?clean=true&offset=0&limit=100"
```

RUN_ID, STORE_ID and DATASET_ID are response identifiers, not input parameters.
On Windows use curl.exe and the appropriate shell environment-variable syntax.
