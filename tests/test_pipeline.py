from azuredevmonitor import request_builder as rb
from azuredevmonitor import config
from azuredevmonitor.resources import pipeline
import pytest

class TestConfig:

    @classmethod
    def setup_class(cls):
        cls.cnf = config.get_instance()

    # @pytest.mark.skip()
    def test_list_pipeline(self):

        r = pipeline.Pipeline().get_list()
        assert r.status_code == 200
        assert len(r.json()) > 0