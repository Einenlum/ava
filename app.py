from view import hello_pycon
from http_utils import Request


def wsgi_app(function):
    def wrapper(environ, start_response):
        request = Request.build_from_wsgi(environ)
        response = function(request)
        start_response(response.status, response.headers)

        return iter([response.content])

    return wrapper

@wsgi_app
def my_app(request):
    return hello_pycon(request)
