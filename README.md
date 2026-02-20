# psutierlist-api-wrapper

A fully-typed, modern Python wrapper for the internal API used on [psutierlist.org](https://psutierlist.org/).

> [!WARNING]
> This library is not affiliated with the website or anyone behind SPL's PSU Tier List. It may break at any time if the API changes, due to this being an unofficial wrapper that relies on an undocumented API.

## Installation

This package is on PyPI, so you can use `pip`:

```bash
pip install psutierlist-api-wrapper
```

## Usage

Sync usage:
```python
import psutierlist_api_wrapper as paw

def main() -> None:
    pages = paw.get_pages()  # type is `paw.Response`

if __name__ == "__main__":
    main()
```

Async usage:
```python
import asyncio
import psutierlist_api_wrapper as paw

async def main() -> None:
    pages = await paw.get_pages_async()

if __name__ == "__main__":
    asyncio.run(main())
```

## Docs

I have not written docs yet. The code is pretty simple and self-explanatory, so you can just browse through `psutierlist_api_wrapper/__init__.py` and `psutierlist_api_wrapper/enums.py` at the [GitHub Page](https://github.com/PowerPCFan/psutierlist-api-wrapper) to see how everything is structured. Sorry for the inconvenience!
