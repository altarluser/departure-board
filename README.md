# departure-board

An open-source, Python-based public transportation departure board.

The first planned implementation will show real-time departures in Berlin, using VBB data. Future versions will support other cities and transport API providers.

## Development

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/). The local development
interpreter is pinned to Python 3.11 in `.python-version`.

```sh
uv sync --locked
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

