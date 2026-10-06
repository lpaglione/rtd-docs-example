# Read the Docs example: documenting `client.py` from its docstrings

```
rtd-docs-example/
├── .readthedocs.yaml      <- RTD build recipe (must be at repo root)
├── docs/
│   ├── conf.py            <- Sphinx settings (autodoc, theme, mocks)
│   ├── index.rst          <- home page + table of contents
│   ├── api.rst            <- ".. automodule:: client" = the docstring magic
│   └── requirements.txt   <- what RTD pip-installs before building
└── src/
    └── client.py          <- the code being documented
```

## Publish on Read the Docs
1. Push this folder to a GitHub repo (the folder's contents at the repo root).
2. Sign in at https://app.readthedocs.org with GitHub -> "Add project" -> pick the repo.
3. RTD reads `.readthedocs.yaml`, installs `docs/requirements.txt`, runs Sphinx, and
   publishes at `https://<project>.readthedocs.io`. Every push rebuilds it.

## Preview locally (Mac terminal)
```
cd rtd-docs-example
python3 -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
open docs/_build/html/index.html
```
