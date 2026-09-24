# Contributing

Contributions should improve the examples, documentation or data-format clarity without adding credentials, private endpoints or unsupported promises about the hosted Actor.

Before opening a pull request:

- Run every example against a safe, low-cost input.
- Check JSON and CSV examples against the current public output schema.
- Run `python scripts/validate_input_contract.py`; when the Actor source checkout is available, also pass its current `.actor/input_schema.json` with `--actor-schema`.
- Keep the README factual and aligned with the Actor page.
- Do not commit tokens, proxy URLs, cookies, logs or private run data.
