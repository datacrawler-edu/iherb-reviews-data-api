# iHerb reviews API: Python, JSON and CSV examples

Collect customer review rows from the hosted iHerb Reviews Extractor using product
URLs or IDs. This integration guide covers a small request, sequential product
workflows and exporting an existing review Dataset to CSV.

[Open iHerb Reviews Extractor on Apify](https://apify.com/datascraperes/iherb-reviews-extractor?fpr=edudata)

## What this repository helps you do

- Retrieve one row per unique product-and-review pair for feedback analysis.
- Export ratings, review titles, text and dates to a spreadsheet.
- Collect bounded review samples from several product links or IDs.
- Request photo reviews and keep the source photo URLs in JSON.

## Example result

Selected fields from the complete sanitized real review samples:

```json
{
  "recordType": "review",
  "productId": 61864,
  "reviewId": "cd2f5459-8c0e-452c-99b4-1aafff050f6f",
  "rating": 5.0,
  "title": "Quali®-C from Europe has disappeared.",
  "language": "ko-KR",
  "verifiedPurchase": true
}
```

[sample-output.json](data/sample-output.json) contains the full two-row snapshot;
reviewer display names are null. [sample-output.csv](data/sample-output.csv) exports
scalar columns. These samples illustrate the output shape, not current reviews.

## Run without code

1. Open the [hosted Actor](https://apify.com/datascraperes/iherb-reviews-extractor?fpr=edudata) and select Input.
2. Paste a product URL, review URL or numeric product ID into Products.
3. Start with 2 total reviews and 2 per product; optionally select photo reviews.
4. Review pricing, click Start, then inspect Dataset and Run summary.
5. Export JSON, CSV or Excel. Check `RUN_SUMMARY.complete` before using a run as complete.

See the [no-code walkthrough](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify's [Free plan](https://apify.com/pricing?fpr=edudata) provides USD5 in monthly prepaid usage and needs no
credit card to start. Available credit can fund a small test; usage is not
unlimited. Unused credits expire at the end of the billing cycle.

## Quick start for developers

Use Python3.10+ or Node.js22+. From the repository root:

```bash
python -m pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/collect_reviews.py
```

PowerShell token setup:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

The example starts one paid-capable run, capped at USD0.01, with the small input.
The client is pinned. Starts are sent once; SDK reads may retry. If a start
response is lost, inspect recent Console runs before starting again.

## Input example

```json
{
  "products": [
    "61864"
  ],
  "maxReviews": 2,
  "maxReviewsPerProduct": 2,
  "reviewsWithPhotosOnly": false
}
```

This includes all four public inputs. Products can also contain full URLs such as
`https://www.iherb.com/pr/california-gold-nutrition-gold-c-usp-grade-vitamin-c-1-000-mg-60-veggie-capsules/61864`.
Equivalent URLs and IDs within one run are combined. See the [field reference](docs/input-reference.md).

## Request examples

| Workflow | Example |
|---|---|
| One bounded review request | [collect_reviews.py](examples/python/collect_reviews.py) |
| Two sequential product requests | [batch_product_reviews.py](examples/python/batch_product_reviews.py) |
| Existing Dataset to CSV, with no new run | [export_reviews_csv.py](examples/python/export_reviews_csv.py) |
| Node.js start, summary and paginated JSON | [request.mjs](examples/javascript/request.mjs) |
| Explicit HTTP start and read-only polling | [cURL guide](examples/curl-request.md) |

```bash
python examples/python/batch_product_reviews.py
python examples/python/export_reviews_csv.py YOUR_DATASET_ID --output data/exported-reviews.csv
node examples/javascript/request.mjs
```

The batch example starts two separately billed runs, each capped at USD0.01.
The CSV example only reads existing data; it never starts an Actor run. Exported
CSV contains scalar fields; use JSON for complete image arrays.

## Output fields

| Field | Meaning |
|---|---|
| `recordType`, `productId`, `reviewId` | Review type and product/review identity. |
| `rating`, `ratingRaw` | Normalized stars and the source-provided rating. |
| `title`, `text`, `date` | Review content and posted date, when supplied. |
| `language`, `translatedTo` | Original language code and translation target, when supplied. |
| `verifiedPurchase`, `helpfulYes`, `helpfulNo` | Purchase-verification flag and helpful votes. |
| `country`, `author` | Optional public source context; fields may be null. |
| `images` | Source photo URLs grouped by available size; files are not downloaded. |
| `productUrl`, `scrapedAt` | Product link and collection timestamp. |

Review IDs are deduplicated together with product IDs within one run.
The separate key-value record `RUN_SUMMARY` reports delivered counts, status,
coverage and reasons for incomplete collection. [Output reference](docs/output-reference.md).

## Common use cases

- Compare themes in product feedback and recurring complaints.
- Prepare a review-text and rating dataset for sentiment analysis.
- Inspect customer-photo reviews using their source links.
- Export existing review datasets without another collection request.

## Export iHerb review text and ratings to CSV

Save a completed run's Dataset ID, then run the CSV example. It reads pages in
order and advances by the actual number received until the final empty page.
UTF-8 CSV preserves multilingual text and quoted newlines. Keep JSON when you
need nested image arrays. [Workflow details](docs/use-cases.md).

## Collect reviews from several product links

You can put several products in one Actor input and use both limits, or use the
sequential batch script for separately named product collections. A separate
run is a new extraction and can be billed again. This example does not promise
that repeated runs contain only new reviews.

## FAQ

**Does this repository run the scraper locally?** It calls the hosted Actor.

**Can I pass product URLs?** Yes: product/review links or numeric IDs, up to100entries.

**Can I select a translation language or star rating?** Those are not public inputs.
Text is returned as supplied by iHerb and may already be translated; inspect
`language` and `translatedTo` rather than assuming original-language text.

**Does it download photos?** It returns URLs. Photo selection is optional.

**Why can a successful run have incomplete collection?** Input corrections,
spending limits and source/time limits can produce incomplete summaries. The
examples require `complete:true` before processing a run as complete.

See [more answers](docs/faq.md).

## Limits and pricing

Collection is bounded: up to100product inputs,20,000requested reviews per run and
10,000per product. Zero does not mean unlimited. Source availability,ordering,
repeated pages and execution limits can reduce delivery. This is not an
exhaustive historical archive guarantee.

`review-result` is a pay-per-event charge for each unique review saved and
available in the Dataset. There is no product or start event. These are the
verified configured prices; check the [hosted pricing](https://apify.com/datascraperes/iherb-reviews-extractor?fpr=edudata) before starting.

| Plan | Price per delivered review | Equivalent per 1,000 reviews |
|---|---:|---:|
| FREE | $0.0005 | $0.5 |
| BRONZE | $0.00045 | $0.45 |
| SILVER | $0.0004 | $0.4 |
| GOLD | $0.000375 | $0.375 |
| PLATINUM | $0.000375 | $0.375 |
| DIAMOND | $0.000375 | $0.375 |

Use a spending cap. Failed requests,duplicate reviews within the same run and
summaries do not create review events. Already delivered reviews remain
billable even if a later source page cannot be collected.

## Hosted version

Use [iHerb Reviews Extractor on Apify](https://apify.com/datascraperes/iherb-reviews-extractor?fpr=edudata) for the maintained service.
This repository contains documentation and API examples only. For product
discovery,prices and nested review samples,see the separate
[product API examples](https://github.com/datacrawler-edu/iherb-product-data-api).

## Responsible use

Use public review data lawfully,follow applicable source terms and retain only
the content needed for your purpose. Reviewer names may be personal data;
the supplied public samples omit them. Avoid profiling or contacting individuals.

## Support

For example-code issues,open a [GitHub issue](https://github.com/datacrawler-edu/iherb-reviews-data-api/issues). For a hosted run,
use the [Actor's Issues tab](https://apify.com/datascraperes/iherb-reviews-extractor?fpr=edudata) with the run ID,input and expected behavior.
Never post tokens or private customer data.

Some Apify links are affiliate links (`fpr=edudata`).

## License

These documentation and integration examples are available under the [MIT license](LICENSE).
