from http_utils import Request
from dataclasses import dataclass, field
from typing import Callable, Optional
from http_utils import Response
import re

@dataclass
class Route:
    path: str
    view: Callable
    options: Optional[dict] = field(default_factory=dict)

@dataclass
class CompiledRoute:
    regex: str
    view: Callable
    options: dict

def call_view(request: Request, route_declarations: list) -> Response:
    routes = _compile_routes(route_declarations)
    for route in routes:
        if matches := re.match(route.regex, request.path):
            if 'methods' not in route.options or request.method in route.options['methods']:
                return route.view(request=request, **matches.groupdict())

    return Response('Not found', 404)

def _compile_routes(route_declarations: list):
    compiled_routes = []
    for declaration in route_declarations:
        regex = re.sub(r'{([^}]+)}', r'(?P<\g<1>>[a-zA-Z0-9%_-]+)', declaration.path)
        regex = r'^' + regex + r'$'

        compiled_routes.append(CompiledRoute(regex, declaration.view, declaration.options))

    return compiled_routes
