# Frequently asked questions

## Is this an official iHerb API?

It is an integration with the [hosted Apify Actor](https://apify.com/datascraperes/iherb-reviews-extractor?fpr=edudata),not an iHerb-affiliated service.

## URLs or product IDs?

Both are supported in products. Equivalent identities are combined within one
run. The second input field is the total review cap,not a product count.

## What is billed?

Each unique review delivered through review-result. There is no product/start
event. A new run is a new extraction; inspect current hosted pricing first.

## Does a successful process prove a complete dataset?

Read RUN_SUMMARY.complete. The examples reject incomplete/missing summaries
while leaving the saved Dataset accessible for inspection/export.

## Can I automatically retry a failed start?

A lost start response may still have created a paid run. These examples send
one POST and instruct you to inspect Console before another start. Read-only
polling/export requests can retry without starting another extraction.

## Can I request all reviews or choose a language?

Limits are finite and source-dependent. Arbitrary language,star,country,date
and sort filters are not public inputs. Inspect translation fields in results.

## Do I need a paid Apify plan?

The [Free plan](https://apify.com/pricing?fpr=edudata) offers monthly prepaid credit without a card to start;
available credit can fund a small test. It is not unlimited usage.
