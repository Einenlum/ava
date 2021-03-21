from http_utils import Request
from importlib import import_module
import os
import routing

def get_routes():
    module_path, app_name = os.environ['APP_PATH'].split(':')
    module = import_module(module_path)
    routes = getattr(module, app_name)

    return routes()


def framework_app(environ, start_response):
    request = Request.build_from_wsgi(environ)
    routes = get_routes()
    response = routing.call_view(request, routes)
    start_response(response.status, response.headers)

    return iter([response.content])
