# Use cases

## Topic and competitor course research

Submit the topics you want to compare and set a shared unique-course target.

```json
{
  "searchTerms": ["python", "data science"],
  "maxItems": 20,
  "freeOnly": false,
  "includeCourseDetails": false
}
```

Inspect `title`, `url`, `ratingAverage`, `ratingCount`, `instructors`, `durationSeconds` and the generated `sourceSearchUrl`.

## Price and rating snapshots

Run the same terms periodically with a small `maxItems` value and store the Dataset exports with `scrapedAt`.

```json
{
  "searchTerms": ["python"],
  "maxItems": 10,
  "freeOnly": false,
  "includeCourseDetails": false
}
```

Compare `price.amount`, `price.currency`, `price.priceString`, `ratingAverage` and `ratingCount`. These are time- and market-sensitive public snapshots, not permanent price guarantees.

## Free-course discovery and catalog enrichment

Enable `freeOnly` to focus on courses marked as free, and enable optional detail enrichment when the catalog needs public descriptions, language, offers, syllabus sections or audience information.

```json
{
  "searchTerms": ["python"],
  "maxItems": 5,
  "freeOnly": true,
  "includeCourseDetails": true
}
```

Inspect `description`, `datePublished`, `availableLanguage`, `inLanguage`, `educationalLevel`, `offers`, `syllabusSections`, `teaches`, `audience` and `detailStatus`. Optional fields remain unavailable when the public course page does not expose them.
