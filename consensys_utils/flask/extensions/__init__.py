"""
    consensys_utils.flask.extensions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Declares flask extensions

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

__all__ = [
    'initialize_extensions',
]


def initialize_health_extension(app):
    """Initialize healthcheck extension

    If ``health`` is missing in application configuration then this function has no effect

    :param app: Flask application
    :type app: :class:`flask.Flask`
    """
    if 'health' in app.config:  # pragma: no branch
        from .health import health
        health.init_app(app)


def initialize_web3_extension(app):
    """Initialize Web3 extension

    If ``web3`` is missing in application configuration then this function has no effect

    :param app: Flask application
    :type app: :class:`flask.Flask`
    """
    if 'web3' in app.config:  # pragma: no branch
        from .web3 import web3
        web3.init_app(app)


DEFAULT_EXTENSIONS = [
    initialize_health_extension,
    initialize_web3_extension,
]


def initialize_extensions(app, extensions=None):
    """Initialize extensions on a Flask application

    Example: Adding an extension

    .. doctest::
        >>> from flask import Flask
        >>> from flasgger import Swagger

        >>> app = Flask(__name__)

        >>> swag = Swagger(template={'version': '0.3.4-dev'})

        >>> my_extensions = [swag]

        >>> initialize_extensions(app, my_extensions)

    :param app: Flask application
    :type app: :class:`flask.Flask`
    :param extensions: Extensions to initialize on the application.
        Expects a list of elements which are either

        - a Flask extension object (having a callable attribute ``init_app``)
        - a function that takes a :class:`flask.Flask` as argument and eventually initialize an extension on it
    :type extensions: list
    """

    extensions = extensions or []

    # Initialize extensions
    for extension in extensions:
        if hasattr(extension, 'init_app') and callable(extension.init_app):
            extension.init_app(app)
        else:
            extension(app)
