from zeus import request_builder as rb
from zeus import config
import pytest


def test_request():
    assert(rb.request_ok(rb.get(config.get_default_setting("URL"))))

    