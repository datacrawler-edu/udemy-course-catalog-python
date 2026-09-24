# Input reference

The Actor accepts keywords and phrases. It constructs the public Udemy search requests internally.

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `searchTerms` | array of strings | Yes | `["python", "data science"]` | 1–10 unique keywords or phrases, each up to 200 characters. |
| `maxItems` | integer | No | `3` | Maximum number of unique courses across all terms. Default `100`; range `1`–`10000`. |
| `freeOnly` | boolean | No | `false` | Limit the public catalog to courses marked as free. Default `false`. |
| `includeCourseDetails` | boolean | No | `false` | Request available structured fields from each public course page. Default `false`; increases request count and run time. |

## Smallest useful input

```json
{
  "searchTerms": ["python"],
  "maxItems": 3,
  "freeOnly": false,
  "includeCourseDetails": false
}
```

## Validation and limits

- `searchTerms` must contain 1–10 non-empty keywords or phrases.
- Terms are whitespace-normalized and duplicate terms are removed case-insensitively.
- URLs are not accepted as search terms; the Actor creates the public search requests internally.
- `maxItems` is a unique-course limit across all submitted terms, not a page limit.
- Pagination continues until the target is reached or the public catalog is exhausted.
