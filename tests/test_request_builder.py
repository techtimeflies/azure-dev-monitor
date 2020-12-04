from zeus import request_builder as rb
from zeus import config
import pytest

class TestConfig():
    def setup_class(cls):
        cls.cnf=config.get_instance()

    def test_request(self):
        assert(rb.request_ok(rb.get(self.cnf.get_default_setting("URL"))))

    