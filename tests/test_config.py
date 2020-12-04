from zeus import config
import pytest

def test_config_exists():
    assert config.config_exists()

def test_get_config():
    assert config.get_config() is not None
    assert len(config.get_config()) > 0


def test_read_default_setting():
    assert config.get_default_setting("URL") is not None


def test_read_setting():
    assert config.get_setting("API_VERSION", "DEFAULT") is not None