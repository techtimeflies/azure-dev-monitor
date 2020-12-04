from zeus import config

def test_config_exists():
    assert config.config_exists()

def test_read_default_setting():
    assert config.get_default_setting("URL") is not None

def test_read_setting():
    assert config.get_setting("API_VERSION", "DEFAULT") is not None