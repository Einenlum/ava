from http_utils import Request, Response


def hello_pycon(request: Request):
    name = request.query.get('name') or 'default'

    return Response(Response.HTTP_OK, f'<html><h1>Hello, {name}</h1></html>')
