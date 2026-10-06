"""Improved-documentation example for pySAML2's ``Saml2Client``.

This module is a *teaching example*, not part of pySAML2. It contains a copy
of ``Saml2Client.prepare_for_authenticate`` from ``client.py`` with the same
code but a rewritten docstring and type hints, to show what thorough API
documentation for this kind of code can look like.

The docstring uses the Google style (``Args:``, ``Returns:``, ``Raises:``,
``Example:``), which Sphinx reads through its ``napoleon`` extension.

.. note::
   The behaviour described here was inferred by Claude (an AI assistant)
   from reading the code and has not been verified by the pySAML2
   maintainers.
"""

from __future__ import annotations  # lets "str | None" hints work on older Pythons

import saml2
from saml2.client_base import Base


class Saml2Client(Base):
    """A SAML 2.0 Service Provider (SP) client.

    Use this class in a web application that needs users to log in through
    a SAML Identity Provider (IdP). It builds the requests your application
    sends to IdPs and processes the responses they send back.

    A typical login flow:

    1. Call :meth:`prepare_for_authenticate` to build an authentication
       request and send the user's browser to the IdP.
    2. When the IdP posts back, pass its response to
       :meth:`client_base.Base.parse_authn_request_response`.

    Most of the request-building and response-parsing machinery is
    inherited from :class:`client_base.Base`.
    """

    def prepare_for_authenticate(
        self,
        entityid: str | None = None,
        relay_state: str = "",
        binding: str = saml2.BINDING_HTTP_REDIRECT,
        vorg: str = "",
        nameid_format: str | None = None,
        scoping=None,
        consent: str | None = None,
        extensions=None,
        sign: bool | None = None,
        sigalg: str | None = None,
        digest_alg: str | None = None,
        response_binding: str = saml2.BINDING_HTTP_POST,
        **kwargs,
    ) -> tuple[str, dict]:
        """Build a SAML authentication request to send a user to their IdP.

        This is usually the first step of a login: call it when an
        unauthenticated user arrives, then send their browser to the IdP
        using the returned HTTP info. When the IdP replies, pass its response
        to :meth:`client_base.Base.parse_authn_request_response`.

        Args:
            entityid: Entity ID of the IdP to authenticate against. If
                omitted, the IdP must be determinable from configuration.
            relay_state: Opaque value the IdP sends back unchanged;
                typically the URL to return the user to after login.
            binding: How to send the request to the IdP (HTTP-Redirect or
                HTTP-POST). The IdP's metadata must support this binding.
            vorg: Entity ID of a virtual organization the SP belongs to, if
                any.
            nameid_format: The NameID format to ask the IdP for, e.g.
                ``saml2.saml.NAMEID_FORMAT_PERSISTENT``.
            scoping: Optional ``<Scoping>`` element limiting which IdPs may
                handle the request (used with IdP proxies).
            consent: Consent URI indicating whether the user agreed to the
                request.
            extensions: Optional ``<Extensions>`` element to include in the
                request.
            sign: Whether to sign the request. ``None`` uses the configured
                default.
            sigalg: Signature algorithm URI, e.g.
                ``saml2.xmldsig.SIG_RSA_SHA256``. Only used if ``sign`` is
                true.
            digest_alg: Digest algorithm URI used in the signature.
            response_binding: The binding the IdP should use to send its
                response back (normally HTTP-POST).
            **kwargs: Passed through to
                :meth:`client_base.Base.create_authn_request`.

        Returns:
            A ``(request_id, http_info)`` tuple. Store ``request_id`` so the
            response can be matched to this request. ``http_info`` holds the
            URL, headers and/or form to send to the user's browser.

        Raises:
            SignOnError: The IdP supports none of the requested bindings.
            ValueError: The binding actually used differs from ``binding``.

        Example:
            >>> req_id, info = client.prepare_for_authenticate(
            ...     entityid="https://idp.example.org/idp",
            ...     relay_state="/dashboard",
            ... )
            >>> outstanding[req_id] = "/dashboard"
            >>> redirect_url = dict(info["headers"])["Location"]
        """
        reqid, negotiated_binding, info = self.prepare_for_negotiated_authenticate(
            entityid=entityid,
            relay_state=relay_state,
            binding=binding,
            vorg=vorg,
            nameid_format=nameid_format,
            scoping=scoping,
            consent=consent,
            extensions=extensions,
            sign=sign,
            sigalg=sigalg,
            digest_alg=digest_alg,
            response_binding=response_binding,
            **kwargs,
        )

        if negotiated_binding != binding:
            raise ValueError(f"Negotiated binding '{negotiated_binding}' does not match binding to use '{binding}'")

        return reqid, info
