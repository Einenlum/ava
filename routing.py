from http_utils import Request
from dataclasses import dataclass
from typing import Callable
from http_utils import Response
import re

@dataclass
class CompiledRoute:
    regex: str
    view: Callable

def call_view(request: Request, route_declarations: list) -> Response:
    routes = _compile_routes(route_declarations)
    for route in routes:
        if matches := re.match(route.regex, request.path):
            return route.view(request=request, **matches.groupdict())

    return Response('Not found', 404)

def _compile_routes(route_declarations: list):
    compiled_routes = []
    for declaration in route_declarations:
        (path, view) = declaration

        regex = re.sub(r'{([^}]+)}', r'(?P<\g<1>>[a-zA-Z0-9%_-]+)', path)
        regex = r'^' + regex + r'$'

        compiled_routes.append(CompiledRoute(regex, view))

    return compiled_routes
