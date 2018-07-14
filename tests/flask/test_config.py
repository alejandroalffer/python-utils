"""
    tests.flask.test_config
    ~~~~~~~~~~~~~~~~~~~~~~~

    Test Flask configuration features

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see LICENSE for more details.
"""

import os

import pytest
from cfg_loader import ConfigSchema
from marshmallow import fields

from consensys_utils.flask import Flask
from consensys_utils.flask.config import set_app_config


@pytest.fixture(scope='session')
def config_file(files_dir):
    yield os.path.join(files_dir, 'config.yml')


class ConfigSchemaTest(ConfigSchema):
    """Config schema for test"""
    param = fields.Str()


@pytest.fixture(scope='function')
def app(config_file):
    _app = Flask(__name__, config_schema=ConfigSchemaTest)

    set_app_config(_app, config_file)

    yield _app


def test_config(config):
    assert 'param' in config and config['param'] == 'test-value'
