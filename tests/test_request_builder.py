from azuredevmonitor import request_builder as rb
from azuredevmonitor import config
import pytest

class TestConfig():
    def setup_class(cls):
        cls.cnf=config.get_instance()

    @pytest.mark.skip
    def test_request(self):
        assert(rb.request_ok(rb.get("")))

    @pytest.mark.skip()
    def test__build_api(self):
        assert(rb.request_ok(rb.get(self.cnf.get_default_setting("URL"))))

    