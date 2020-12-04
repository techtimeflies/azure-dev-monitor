from zeus import request_builder as rb

def test_request():
    assert(rb.request_ok(rb.get('https://www.google.com')))

    