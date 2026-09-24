# Input reference

The Actor accepts keywords and phrases. It constructs the public Udemy search requests internally.

In the Apify web interface, Udemy-specific filters are presented as predefined dropdowns or multiselects. Language selectors show readable names such as `English (EN)` and `Spanish (ES)` while sending the ISO-639-1 code internally. Users select valid options instead of typing filter codes. API and JSON callers must send the exact enum values shown here.

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `searchTerms` | array of strings | Yes | `["python", "data science"]` | 1–10 unique keywords or phrases, each up to 200 characters. |
| `maxItems` | integer | No | `3` | Maximum number of unique courses across all terms. Default `100`; range `1`–`10000`. |
| `freeOnly` | boolean | No | `false` | Limit the public catalog to courses marked as free. Default `false`. |
| `sortOrder` | string | No | `"RATING"` | Dropdown in Apify. Result order: `RELEVANCE`, `REVIEWS`, `RATING` or `TIME`. Default `RELEVANCE`. |
| `languages` | array of strings | No | `["EN"]` | Multiselect showing names plus ISO-639-1 codes, such as `English (EN)` and `Spanish (ES)`. Up to 10 values. |
| `levels` | array of strings | No | `["BEGINNER"]` | Multiselect with `ALL_LEVELS`, `BEGINNER`, `INTERMEDIATE` and `EXPERT`. Up to 10 values. |
| `minRating` | number | No | `4.5` | Number from 0 to 5 in half-point increments. |
| `videoLengths` | array of strings | No | `["SHORT", "MEDIUM"]` | Multiselect with `EXTRA_SHORT`, `SHORT`, `MEDIUM`, `LONG` and `EXTRA_LONG`. |
| `closedCaptionLanguages` | array of strings | No | `["EN"]` | Multiselect showing caption language names plus ISO-639-1 codes. Up to 10 values. |
| `mustHaveClosedCaptions` | boolean | No | `false` | Checkbox to require closed captions. |
| `mustHaveQuizzes` | boolean | No | `false` | Require quizzes. |
| `mustHaveCodingExercises` | boolean | No | `false` | Require coding exercises. |
| `mustHavePracticeTests` | boolean | No | `false` | Require practice tests. |
| `mustHaveWorkspaces` | boolean | No | `false` | Require workspaces. |
| `mustHaveRoleplays` | boolean | No | `false` | Require roleplay activities. |
| `practiceTestCoursesOnly` | boolean | No | `false` | Return only practice-test courses. |
| `certificationPrepOnly` | boolean | No | `false` | Return only certification-preparation courses. |
| `includeCourseDetails` | boolean | No | `false` | Request available structured fields from each public course page. Default `false`; increases request count and run time. |

## Complete input contract

This valid JSON includes every public input property. Empty selector arrays and `false` flags leave optional filters disabled.

<!-- apify-input-example:complete -->
```json
{
  "searchTerms": [
    "python"
  ],
  "maxItems": 3,
  "freeOnly": false,
  "sortOrder": "RELEVANCE",
  "languages": [],
  "levels": [],
  "minRating": 0,
  "videoLengths": [],
  "closedCaptionLanguages": [],
  "mustHaveClosedCaptions": false,
  "mustHaveQuizzes": false,
  "mustHaveCodingExercises": false,
  "mustHavePracticeTests": false,
  "mustHaveWorkspaces": false,
  "mustHaveRoleplays": false,
  "practiceTestCoursesOnly": false,
  "certificationPrepOnly": false,
  "includeCourseDetails": false
}
```

## Smallest useful input

```json
{
  "searchTerms": ["python"],
  "maxItems": 3,
  "freeOnly": false,
  "sortOrder": "RELEVANCE",
  "includeCourseDetails": false
}
```

## Validation and limits

- `searchTerms` must contain 1–10 non-empty keywords or phrases.
- Terms are whitespace-normalized and duplicate terms are removed case-insensitively.
- URLs are not accepted as search terms; the Actor creates the public search requests internally.
- Language codes are normalized case-insensitively and must be valid ISO-639-1 two-letter codes.
- Filter arrays accept at most 10 values; duplicate values are removed.
- `maxItems` is a unique-course limit across all submitted terms, not a page limit.
- Pagination continues until the target is reached or the public catalog is exhausted.
