from http_utils import Request, Response, TemplateResponse
import json

def hello_pycon(request: Request):
    name = request.query.get('name') or 'default'

    return TemplateResponse('index.html', {'name': name})

def article(request: Request, article_slug: str):
    return Response(f'<html><h1>Article, {article_slug}</h1></html>')

def post_article(request: Request):
    try:
        content = json.loads(request.body)
    except ValueError:
        content = {}

    title = content.get('title', 'undefined')

    return Response(f'<html><h1>Article "{title}" created!</h1></html>')
