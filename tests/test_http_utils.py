import pytest
from http_utils import Request, Response

class FakeWsgiBody:
    def __init__(self, content):
        self._content = content

    def read(self) -> bytes:
        return self._content

def test_the_request_parses_querystrings():
    environ = {
        'QUERY_STRING': 'foo=lol&bar=baz&empty',
        'RAW_URI': r'/article',
        'wsgi.input': FakeWsgiBody(b'Hi, this is a body content'),
        'REQUEST_METHOD': 'GET'
    }

    request = Request.build_from_wsgi(environ)

    assert request.path == r'/article'
    assert request.query.get('foo') == 'lol'
    assert request.query.get('bar') == 'baz'
    assert request.query.get('empty') == None
    assert request.query.get('non-existant') == None
    assert request.body == 'Hi, this is a body content'


def test_the_response_gives_accurate_status():
    expected_answers = (
        (200, '200 OK'),
        (409, '409 Conflict'),
        (404, '404 Not Found'),
    )

    for (code, description) in expected_answers:
        assert Response('Some content', status=code).status == description

def test_a_response_is_created_with_the_right_headers():
    response = Response('Some content', 403)

    assert response.content == b'Some content'
    assert response.status == '403 Forbidden'
    assert response.headers == [
        ('Content-Type', 'text/html; charset=utf8'),
        ('Content-Length', '12')
    ]
