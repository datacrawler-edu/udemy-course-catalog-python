# Use cases

## Topic and competitor course research

Submit search URLs for the topics you want to compare and set a shared unique-course target.

```json
{
  "searchUrls": [
    "https://www.udemy.com/courses/search/?q=python",
    "https://www.udemy.com/courses/search/?q=data+science"
  ],
  "maxItems": 20,
  "includeCourseDetails": false
}
```

Inspect `title`, `url`, `ratingAverage`, `ratingCount`, `instructors`, `durationSeconds` and `sourceSearchUrl`.

## Price and rating snapshots

Run the same search URL periodically with a small `maxItems` value and store the Dataset exports with `scrapedAt`.

```json
{
  "searchUrls": [
    "https://www.udemy.com/courses/search/?src=ukw&q=python"
  ],
  "maxItems": 10,
  "includeCourseDetails": false
}
```

Compare `price.amount`, `price.currency`, `price.priceString`, `ratingAverage` and `ratingCount`. These are time- and market-sensitive public snapshots, not permanent price guarantees.

## SEO or training-catalog enrichment

Enable optional detail enrichment when the catalog needs public descriptions, language, offers, syllabus sections or audience information.

```json
{
  "searchUrls": [
    "https://www.udemy.com/courses/search/?q=python"
  ],
  "maxItems": 5,
  "includeCourseDetails": true
}
```

Inspect `description`, `datePublished`, `availableLanguage`, `inLanguage`, `educationalLevel`, `offers`, `syllabusSections`, `teaches`, `audience` and `detailStatus`. Optional fields remain unavailable when the public course page does not expose them.
