from http_utils import Request
from importlib import import_module
import os

def get_app():
    module_path, app_name = os.environ['APP_PATH'].split(':')
    module = import_module(module_path)
    func = getattr(module, app_name)

    return func


def framework_app(environ, start_response):
    request = Request.build_from_wsgi(environ)
    app = get_app()
    response = app(request)
    start_response(response.status, response.headers)

    return iter([response.content])
