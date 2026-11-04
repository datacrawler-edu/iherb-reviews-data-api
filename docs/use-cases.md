# Review integration workflows

## Feedback and sentiment datasets

Collect small bounded product samples,then use text,rating and date in your
analysis. Treat translatedTo/language carefully and do not infer reviewer identity.

## Multiple products

Use one request with several products and a per-product cap,or run the sequential
[batch script](../examples/python/batch_product_reviews.py). Separate runs are
separately billed. Cross-run deduplication belongs in the downstream workflow
and does not cancel hosted charges for a new collection.

## Existing Dataset to CSV

The [export script](../examples/python/export_reviews_csv.py) starts no run.
It pages through existing data and writes UTF-8 CSV. Keep the existing Dataset
ID so a transient export problem can be investigated without collecting again.

## Customer photos

Enable reviewsWithPhotosOnly to request the source photo selection. JSON keeps
image URLs; this example does not download images or guarantee their retention.
