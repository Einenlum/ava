import pytest
from http_utils import Request, Response

def test_the_request_parses_querystrings():
    environ = {'QUERY_STRING': 'foo=lol&bar=baz&empty'}

    request = Request.build_from_wsgi(environ)

    assert request.query.get('foo') == 'lol'
    assert request.query.get('bar') == 'baz'
    assert request.query.get('empty') == None
    assert request.query.get('non-existant') == None


def test_the_response_gives_accurate_status():
    expected_answers = (
        (200, '200 OK'),
        (409, '409 Conflict'),
        (404, '404 Not Found'),
    )

    for (code, description) in expected_answers:
        assert Response('Some content', status=code).status == description
