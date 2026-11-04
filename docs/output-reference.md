# Review rows and collection status

Each Dataset row is a review with recordType,productId,reviewId,productUrl and
scrapedAt. The product/review pair is its identity. Optional fields include
rating,ratingRaw,title,text,date,language,translatedTo,country,verifiedPurchase,
helpfulYes,helpfulNo,author and images. Source fields can be null. Photos contain
small/medium/large URL variants and assetId when available; they are not fetched.

See the [complete real snapshot](../data/sample-output.json). Reviewer display
names are replaced with null in this public snapshot. CSV shows scalar fields;
JSON retains arrays. The source may already supply translated text,so the
language code alone does not guarantee that the text is in that language.

RUN_SUMMARY is a separate key-value record,not a review row. Inspect complete,
status,reviewsDelivered,stopReason and errors. complete:true means requested
limits were reached or exposed pages were processed without a collection
problem; it is not proof of every historical review. Input correction may end
normally with input_needs_correction and zero rows. Partial source/spending/time
outcomes preserve saved rows; unresolved required storage/billing state is fatal.
