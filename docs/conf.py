# Sphinx configuration -- this is what Read the Docs runs.
import os
import sys

# 1) Let Sphinx find the Python code. autodoc *imports* the module to read its docstrings.
sys.path.insert(0, os.path.abspath("../src"))

project = "Saml2Client docs example"
author = "IdentityPython"

extensions = [
    "sphinx.ext.autodoc",    # pulls docstrings out of the code
    "sphinx.ext.viewcode",   # adds [source] links next to each documented item
    "sphinx.ext.napoleon",   # understands Google-style docstrings (Args:, Returns:, ...)
]

# 2) client.py imports the pysaml2 package ("saml2"). Instead of installing pysaml2
#    (and its crypto dependencies) on the build server, tell autodoc to fake it.
#    The trade-off: anything inherited from saml2.client_base.Base is NOT documented.
autodoc_mock_imports = ["saml2"]

# 3) Defaults for every ".. automodule::" / ".. autoclass::" directive.
autodoc_default_options = {
    "members": True,           # document functions/classes/methods...
    "undoc-members": True,     # ...including ones with NO docstring (remove to hide them)
    "show-inheritance": True,  # show "Bases: saml2.client_base.Base"
    "member-order": "bysource",
}

html_theme = "sphinx_rtd_theme"
