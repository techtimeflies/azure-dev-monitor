from zeus import request_builder as rb
from zeus import config

def test_request():
    parser = config.parser
    assert(rb.request_ok(rb.get(parser["DEFAULT"]["URL"])))

    