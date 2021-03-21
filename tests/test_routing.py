import pytest
from http_utils import Request, Response
import routing

def view_home(request: Request) -> Response:
    return Response('Homepage')

def view_article(request: Request, slug: str, id: str) -> Response:
    return Response('Some response')

route_declarations = [
    (r'/', view_home),
    (r'/article/{slug}/comment/{id}', view_article)
]

def test_it_compiles_route_declarations():
    routes = routing._compile_routes(route_declarations)
    assert len(routes) is 2
    (home_route, article_route) = routes

    assert home_route.view is view_home
    assert home_route.regex == r'^/$'

    assert article_route.view is view_article
    assert article_route.regex == r'^/article/(?P<slug>[a-zA-Z0-9%_-]+)/comment/(?P<id>[a-zA-Z0-9%_-]+)$'

def test_it_renders_the_right_view():
    request = Request(r'/article/my-slug/comment/12')
    response = routing.call_view(request, route_declarations)

    assert response.status == '200 OK'
    assert response.content == b'Some response' 

    request = Request(r'/')
    response = routing.call_view(request, route_declarations)

    assert response.status == '200 OK'
    assert response.content == b'Homepage' 

def test_it_renders_a_404_if_():
    request = Request(r'/lorem/ipsum')
    response = routing.call_view(request, route_declarations)

    assert response.status == '404 Not Found'
