from view import hello_pycon
from http_utils import Request


def my_application(environ, start_response):
    request = Request.build_from_wsgi(environ)

    response = hello_pycon(request)

    start_response(response.status, response.headers)

    return iter([response.content])
