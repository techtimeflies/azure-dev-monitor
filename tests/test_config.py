from azuredevmonitor import config
import pytest

class TestConfig():
    def setup_class(cls):
        cls.cnf=config.get_instance()

    def test_config_exists(self):
        assert self.cnf.config_exists()

    def test_get_config(self):
        assert self.cnf.get_config() is not None
        assert len(self.cnf.get_config()) > 0


    def test_read_default_setting(self):
        assert self.cnf.get_default_setting("URL") is not None


    def test_read_setting(self):
        assert self.cnf.get_setting("API_VERSION", "DEFAULT") is not None