PyJWT
=====

.. image:: https://travis-ci.com/Privex/pyjwt.svg?branch=master
   :target: http://travis-ci.com/Privex/pyjwt?branch=master

.. image:: https://ci.appveyor.com/api/projects/status/h8nt70aqtwhht39t?svg=true
   :target: https://ci.appveyor.com/project/Privex/pyjwt

.. image:: https://img.shields.io/pypi/v/privex-pyjwt.svg
   :target: https://pypi.python.org/pypi/privex-pyjwt

.. image:: https://coveralls.io/repos/Privex/pyjwt/badge.svg?branch=master
   :target: https://coveralls.io/r/Privex/pyjwt?branch=master

.. image:: https://readthedocs.org/projects/pyjwt/badge/?version=latest
   :target: https://pyjwt.readthedocs.io

This is a fork of https://github.com/jpadilla/pyjwt by `Privex Inc.`_ - allowing us to be able to add our own updates which may
not be accepted upstream in ``jpadilla/pyjwt``

Our fork is published as ``privex-pyjwt`` while the original is published as ``PyJWT`` - the packages are mutually
incompatible, as both use the ``jwt`` top-level namespace.

Notable feature additions by Privex over the original PyJWT package:

* Version 1.8.0
    * Added support for EdDSA (Ed25519) JWT signing and verification


---------------------------------------------------------------------------

A Python implementation of `RFC 7519 <https://tools.ietf.org/html/rfc7519>`_. Original implementation was written by `@progrium <https://github.com/progrium>`_.


Installing
----------

Install with **pip**::


    pip install privex-pyjwt


Install with **pipenv**::


    pipenv install privex-pyjwt


**NOTE**:

To sign/verify with RSA and Ed25519 (EdDSA), the ``cryptography`` package is required.

To sign/verify with EcDSA, the ``ecdsa`` package is required.

Extra packages::

    pip install -U 'cryptography>=2.6' ecdsa
    # or with pipenv
    pipenv install 'cryptography>=2.6' ecdsa


Sponsor Notice
--------------


**This fork was created by Privex. Support it's development by buying a server from us :)**

.. image:: https://cdn.privex.io/img/promo/privex-banner-728.png
   :target: https://www.privex.io
   :align: center



Usage
-----

.. code-block:: python

    >>> import jwt
    >>> encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'

    >>> jwt.decode(encoded, 'secret', algorithms=['HS256'])
    {'some': 'payload'}


Using EdDSA / Ed25519
---------------------

Support for EdDSA / Ed25519 was added as of the `Privex fork <https://github.com/Privex/pyjwt>`_ in Version 1.8.0

Our privex-pyjwt package is compatible with other JWT EdDSA implementations, such as `NodeJS's Jose <https://github.com/panva/jose/>`_ package.
It can sign tokens with Ed25519 keys which can be verified by NodeJS Jose, and verify tokens signed with Ed25519 by NodeJS Jose.




Generating/loading an Ed25519 (EdDSA) key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to be able to easily generate Ed25519, RSA and ECDSA public/private keys from within your Python app, consider 
using `Privex's Python Helpers`_ which includes a cryptography module designed
to make symmetric / asymmetric encryption simple.

Installing Privex Helpers::

    # For a minimal install with just the cryptography dependencies
    # change [full] to [crypto] (though [full] only adds a few small dependencies)
    pip3 install 'privex-helpers[full]'


You can load/generate an Ed25519 private/public key however you want, but we're using `Privex Helpers`_ 's crypto module
as an example (and showcase of our library). 

The below code uses `Privex Helpers`_ to generate an Ed25519 keypair and output the private key to id_ed25519 and the public key to id_ed25519.pub.

If you don't want to save the keys to a file, you can use ``ed_priv, ed_pub = KeyManager.generate_keypair('ed25519')`` instead.


.. code-block:: python


    from privex.helpers import KeyManager

    ed_priv, ed_pub = KeyManager.output_keypair('id_ed25519', 'id_ed25519.pub', alg='ed25519')

    # ed_priv example contents:
    # b'-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEIBy9N4xfv/9qOiKrxwRKeGfO5ab6lSukKHbuC5vaJ1Mg\n-----END PRIVATE KEY-----\n'
    # ed_pub example contents:
    # b'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC4pK2dePGgctIAsh0H/tmUrLzx2Vc4Ltc8TN9nfuChG'


Using privex-pyjwt to encode/decode JWT tokens with EdDSA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Private keys must be in PEM format with PKCS8, while public keys can be in either PEM (PKCS8) format or OpenSSH format (``ssh-ed25519 ........ user@host``).

Simply use ``jwt.encode`` and ``jwt.decode`` as normal, pass in your Ed25519 private key for encoding, the private/public key for decoding, 
and set the algorithm to ``EdDSA``.

.. code-block:: python

    import jwt
    
    # Tokens can only encoded with an Ed25519 private key
    token = jwt.encode({'hello': 'world'}, ed_priv, algorithm='EdDSA')

    # resulting token: b'eyJ0eXAiOiJKV1QiLCJhbGciOiJFZERTQSJ9.eyJoZWxsbyI6IndvcmxkIn0.HEDJTw1jNaz82WuP3O1l5_i-eaaj3DBEKesPUsInSgKuvbav6XaLORERs7wPrmS14DN_WlzDUCn0LmVGl4VlCg'

    # However, tokens can be decoded using EITHER the public key (PEM / OpenSSH) or the private key, 
    # as we can interpolate the public key from the private key
    jwt.decode(token, ed_priv, algorithms=['EdDSA'])

    # Output: {'hello': 'world'}


.. _Privex's Python Helpers: https://github.com/Privex/python-helpers
.. _Privex Helpers: https://github.com/Privex/python-helpers
.. _Privex Inc.: https://www.privex.io/


Command line
------------

Usage::

    pyjwt [options] INPUT

Decoding examples::

    pyjwt --key=secret decode TOKEN
    pyjwt decode --no-verify TOKEN

See more options executing ``pyjwt --help``.


Documentation
-------------

View the full docs online at https://pyjwt.readthedocs.io/en/latest/


Tests
-----

You can run tests from the project root after cloning with:

.. code-block:: sh

    $ python setup.py test
