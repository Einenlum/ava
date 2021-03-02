import pytest
from http_utils import Request

def test_it_parses_querystrings():
    environ = {'QUERY_STRING': 'foo=lol&bar=baz&empty'}

    request = Request.build_from_wsgi(environ)

    assert request.query.get('foo') == 'lol'
    assert request.query.get('bar') == 'baz'
    assert request.query.get('empty') == None
    assert request.query.get('non-existant') == None
