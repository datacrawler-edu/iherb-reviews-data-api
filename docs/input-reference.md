# Input reference

| Field | Type/default | Supported range or meaning |
|---|---|---|
| products | String array; required target | 1–100 product/review URLs or numeric product IDs. Equivalent identities combined. |
| maxReviews | Integer,100 | 1–20,000 total reviews across all products. |
| maxReviewsPerProduct | Integer,10,000 | 1–10,000 per product; the total cap also applies. |
| reviewsWithPhotosOnly | Boolean,false | Request the source photo-review selection. |

The complete bounded example is [sample-input.json](../data/sample-input.json).
Product links may use iHerb country subdomains. URL input identifies the product;
it does not expose arbitrary sort,language,rating,country or date filters.
Zero limits and unsupported fields are invalid. Missing option values use the
defaults above; the small prefills in the form are example values,not defaults.
