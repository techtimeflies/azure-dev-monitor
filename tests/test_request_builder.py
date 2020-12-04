from zeus import request_builder as rb
from zeus import config
import pytest

class TestConfig():
    def setup_class(cls):
        cls.cnf=config.get_instance()

    @pytest.mark.skip
    def test_request(self):
        assert(rb.request_ok(rb.get("")))

    def test_list_pipeline(self):
        api=self.cnf.get_setting("API_VERSION","DEFAULT")

        r=rb.get(f"pipelines?{api}")

        assert r.status_code == 200

    @pytest.mark.skip()
    def test__build_api(self):
        assert(rb.request_ok(rb.get(self.cnf.get_default_setting("URL"))))

    