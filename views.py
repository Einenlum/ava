from http_utils import Request, Response


def hello_pycon(request: Request):
    name = request.query.get('name') or 'default'

    return Response(f'<html><h1>Hello, {name}</h1></html>')

def article(request: Request, article_slug: str):
    return Response(f'<html><h1>Article, {article_slug}</h1></html>')
