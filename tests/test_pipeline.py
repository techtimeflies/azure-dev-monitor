from src import request_builder as rb
from src import config
from src.resources import pipeline
import pytest

class TestConfig():
    def setup_class(cls):
        cls.cnf=config.get_instance()

    def test_list_pipeline(self):

        r=pipeline.get_instance().get_list()
        assert r.status_code == 200
        assert len(r.json()) > 0