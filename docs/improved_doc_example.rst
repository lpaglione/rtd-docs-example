What good documentation can look like
=====================================

This page compares the documentation for **one method**,
``Saml2Client.prepare_for_authenticate``, as it exists today in ``client.py``
with a rewritten version in ``src/improved_doc_example.py``. The code is the
same; only the docstring and type hints differ.

.. note::
   The improved docstring was drafted by Claude (an AI assistant) from reading
   the code. Its description of the method's behaviour has not been verified
   by the pySAML2 maintainers.

What changed
------------

* It opens with **what the method is for and when to call it**.
* It places the method in the **login flow**: what comes next, and what to do with the result.
* It gives **types** through type hints, which Sphinx shows and code editors can use.
* It documents **every parameter**, including the security-relevant signing options.
* It lists the **errors** a caller must handle.
* It includes a short **usage example**.

Before: the current docstring
-----------------------------

Rendered from ``client.py``:

.. automethod:: client.Saml2Client.prepare_for_authenticate
   :no-index:

After: the improved docstring
-----------------------------

Rendered from ``improved_doc_example.py``:

.. automodule:: improved_doc_example

The source behind it
--------------------

This is what a developer writes in the ``.py`` file to produce the rendering above:

.. literalinclude:: ../src/improved_doc_example.py
   :language: python
   :pyobject: Saml2Client.prepare_for_authenticate
   :end-before: reqid, negotiated_binding
