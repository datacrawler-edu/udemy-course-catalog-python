# Output reference

The default Dataset contains one normalized item per unique public course.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `recordType` | string | Yes | Always `course`. |
| `sourceSearchUrl` | string | Yes | Search URL that produced the item. |
| `page` | integer | Yes | Search pagination page associated with the item. |
| `courseId` | string | Yes | Public Udemy course identifier. |
| `title` | string | Yes | Public course title. |
| `url` | string | Yes | Public course landing-page URL. |
| `instructors` | array | Yes | Public instructor IDs and names when available. |
| `learningOutcomes` | array | Yes | Public learning-outcome strings; can be empty. |
| `badges` | array | Yes | Public badge objects; can be empty. |
| `images` | object | Yes | Available public course image URLs. |
| `price` | object / null | Yes | Public price snapshot with amount, currency, display string and list/discount amounts when available; `null` when no public price is exposed. |
| `scrapedAt` | date-time string | Yes | UTC capture time. |
| `headline`, `isFree`, `isPracticeTestCourse`, `locale`, `level` | mixed / nullable | No | Additional search-result metadata. |
| `ratingAverage`, `ratingCount` | number / integer | No | Public rating and review count. |
| `durationSeconds`, `lectureCount`, `practiceTestQuestionsCount` | integer | No | Public duration and curriculum counts. |
| `updatedOn` | string | No | Public course update date when available. |
| `detailStatus` and detail fields | mixed / nullable | No | Optional course-page fields. `detailStatus` is `ok` or `not_available` when enrichment is requested. |

Nullable or missing values mean that the public source did not provide that value during the run; they are not a claim that the course has no such property.
