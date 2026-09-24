import fs from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_API_TOKEN;
if (!token) {
  throw new Error('Set APIFY_API_TOKEN before running this example.');
}

const runInput = JSON.parse(
  await fs.readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'),
);

const client = new ApifyClient({ token });
const run = await client.actor('datascraperes/udemy-course-catalog-scraper').call({ runInput });
const { items } = await client.dataset(run.defaultDatasetId).listItems();

console.log(JSON.stringify(items, null, 2));
