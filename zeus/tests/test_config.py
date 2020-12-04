from zeus import config

def test_config():
    parser = config.parser

    assert parser["DEFAULT"] is not None
    assert parser["API_VERSION"] is not None