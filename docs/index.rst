Saml2Client documentation example
=================================

This site is *an example* of documentation that is generated directly from IdPy pysaml2 code. For this example, the original file ( `pysaml2/src/saml2/client.py <https://github.com/IdentityPython/pysaml2/blob/master/src/saml2/client.py>`_ --- pySAML2's service-provider client) was copied into this repository ( ``src/client.py`` ) so that its docstrings could be interpreted and displayed using Sphinx autodoc and Read the Docs.

.. note::
    client.py imports the rest of pySAML2 (saml2). This example fakes these imports so nothing extra has to be installed. The trade-off is that the generated page for client.py can't show the methods Saml2Client inherits from its parent class (Base). To cover them, client_base.py (where Base is defined) was also copied into ``src/`` and has its own page in the API reference.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api

========
Analysis
========
.. note::
    I asked Claude to evaluate the effectiveness of the docstrings in this example. It is likely that all of thees comments would apply regardless of the method used to extract documentation from the code.

    The results:

I (Claude) counted these across both files (``client.py`` and ``client_base.py``) with a script that reads the code, not from a rendered site. "Public" excludes methods whose names start with an underscore.

.. list-table::
   :header-rows: 1
   :widths: 60 20 20 20

   * - Measure
     - client.py
     - client_base.py
     - Combined
   * - Public functions/methods with a docstring
     - 9 of 12
     - 17 of 23
     - 26 of 35 (74%)
   * - Parameters with a description
     - 52 of 89
     - 69 of 113
     - 121 of 202 (60%)
   * - Error classes with a docstring
     - --
     - 0 of 5
     - 0 of 5
   * - Parameter types given (docstring or type hint)
     - 0
     - 0
     - 0
   * - Methods that document the errors they raise
     - 0
     - 0
     - 0

What works
----------
* **Where docstrings exist, they mostly use one consistent format** (``:param:`` / ``:return:``), so Sphinx turns them into tidy Parameters and Returns sections without any extra configuration.
* **The core request-building methods are the best documented.** ``client_base.Base.create_authn_request`` describes every one of its 15 parameters, and ``create_attribute_query`` explains the four accepted shapes of its ``attribute`` argument.
* **Some docstrings include concrete examples**, such as the sample return value in ``client.Saml2Client.handle_logout_request``.

What a reader of the site would run into
----------------------------------------
* **Gaps cluster around specific features, not randomly.** Whole areas have no explanation: the SOAP queries in ``client.py`` (``do_authz_decision_query``, ``do_assertion_id_request``, ``do_authn_query``) and the ECP methods in ``client_base.py`` (``parse_ecp_authn_response``, ``can_handle_ecp_response``). These show up on the site as bare signatures.
* **Security-relevant options are consistently undocumented.** The signing settings (``sign_alg`` / ``sigalg`` and ``digest_alg``) are explained in only 2 of the 14 public methods that accept them (``create_authn_request`` and ``handle_logout_request``).
* **Some docstrings are placeholders.** ``create_name_id_mapping_request`` lists five parameters with no text (``name_id_policy``, ``name_id``, ``base_id``, ``encrypted_id``, ``destination``) and an empty ``:return:``. ``create_assertion_id_request`` and ``do_logout`` also start straight with ``:param`` lines, so they have no summary sentence.
* **Copy-paste makes the two pages hard to tell apart.** Both files open with the same module description ("Contains classes and functions that a SAML2.0 Service Provider (SP) may use..."), ``Saml2Client`` and ``Base`` share the same one-line description ("The basic pySAML2 service provider class"), and three ``parse_*_response`` methods are all described only as "Verify that the response is OK".
* **Important options are hidden in** ``**kwargs``. ``create_discovery_service_request`` documents ``policy``, ``returnIDParam`` and ``isPassive``, and ``create_attribute_query`` documents ``sp_name_qualifier``, ``name_qualifier`` and ``format``. None of these appear in the method signatures, so a reader has to trust the docstring to know they exist.
* **No types, and no documented errors.** Neither file has type hints or ``:type:`` lines. Between them the methods raise ``ValueError``, ``SAMLError``, ``SignOnError``, ``LogoutError``, ``NoServiceDefined``, ``IdpUnspecified`` and ``HTTPError``, but none of this is documented. The five custom error classes in ``client_base.py`` (for example ``IdpUnspecified`` and ``VerifyError``) have no description of when they occur.
* **Some descriptions are less precise than the code.** ``handle_logout_response`` says it returns a 4-tuple but sometimes returns whatever ``do_logout`` returns. ``is_session_valid`` is described as a "Place holder" in the published docs. ``global_logout``'s summary is "More or less a layer of indirection :-/".
* **Typos show up on the site**, for example "successfull", "BINDIND_SOAP", "BINDING_HTT_POST", "the the" and "Does a attribute".

Documentation purpose
---------------------
Taken together, the docstrings read as notes written by and for the code's maintainers rather than a guide for new users. Coverage is reasonable (roughly three-quarters of public methods), but the content tends to restate *what* a parameter is, not *why or when* you would use a method or how the pieces fit together (for example, how ``Saml2Client`` relates to ``Base``, or which methods make up a complete login or logout flow). That context would likely need to come from hand-written pages, not from docstrings alone.

.. note::
    These findings come from automated analysis by Claude and have not been verified by the pySAML2 maintainers.
