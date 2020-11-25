# -*- coding: utf-8 -*-
# flake8: noqa

"""
JSON Web Token implementation

Minimum implementation based on this spec:
https://self-issued.info/docs/draft-jones-json-web-token-01.html
"""


__title__ = "PyJWT"

__description__ = "JSON Web Token implementation in Python"
__url__ = "https://pyjwt.readthedocs.io"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

__version__ = "2.0.0"
__author__ = "Privex Inc. (Originally by José Padilla)"
__email__ = "packaging@privex.io"
__license__ = "MIT"
__copyright__ = "Copyright 2019 Privex Inc. / Copyright 2015-2018 José Padilla"


from .api_jws import PyJWS
from .api_jwt import (
    PyJWT,
    decode,
    encode,
    get_unverified_header,
    register_algorithm,
    unregister_algorithm,
)
from .exceptions import (
    DecodeError,
    ExpiredSignatureError,
    ImmatureSignatureError,
    InvalidAlgorithmError,
    InvalidAudienceError,
    InvalidIssuedAtError,
    InvalidIssuerError,
    InvalidSignatureError,
    InvalidTokenError,
    MissingRequiredClaimError,
    PyJWKClientError,
    PyJWKError,
    PyJWKSetError,
    PyJWTError,
)
from .jwks_client import PyJWKClient


__all__ = [
    "PyJWS",
    "PyJWT",
    "PyJWKClient",
    "decode",
    "encode",
    "get_unverified_header",
    "register_algorithm",
    "unregister_algorithm",
    # Exceptions
    "DecodeError",
    "ExpiredSignatureError",
    "ImmatureSignatureError",
    "InvalidAlgorithmError",
    "InvalidAudienceError",
    "InvalidIssuedAtError",
    "InvalidIssuerError",
    "InvalidSignatureError",
    "InvalidTokenError",
    "MissingRequiredClaimError",
    "PyJWKClientError",
    "PyJWKError",
    "PyJWKSetError",
    "PyJWTError",
]
