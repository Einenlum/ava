from html import escape
from http.client import responses
import os
from urllib.parse import parse_qs, urlparse
from mako.template import Template
from mako.lookup import TemplateLookup

class Request:
    def __init__(self, path, querystring='', body='', headers={}, method='GET'):
        self._query_bag = QueryBag(parse_qs(querystring))
        self.path = path
        self.body = body
        self.method = method
        self.headers = headers

    @classmethod
    def build_from_wsgi(cls, environ):
        body = environ['wsgi.input'].read() or b''
        method = environ['REQUEST_METHOD']
        headers = {
            'CONTENT_TYPE': environ.get('CONTENT_TYPE', '')
        }

        return Request(
            environ['RAW_URI'],
            querystring=environ['QUERY_STRING'],
            body=body.decode('UTF-8'),
            headers=headers,
            method=method
        )

    @property
    def query(self):
        return self._query_bag

class Response:
    DEFAULT_CONTENT_TYPE = 'text/html; charset=utf8'

    def __init__(self, content, status:int=200):
        status_description = responses.get(status, 'Undefined')
        self.status = f'{status} {status_description}'
        self.content = bytes(content, encoding='utf8')
    
    @property
    def headers(self):
        return [
            ('Content-Type', self.DEFAULT_CONTENT_TYPE),
            ('Content-Length', str(len(self.content)))
        ]

class TemplateResponse:
    def __init__(self, template_name, context, status:int=200):
        self.template_name = template_name
        self.context = context
        self.status = status

    def render(self) -> Response:
        current_dir = os.getcwd()
        lookup = TemplateLookup(directories=[f'{current_dir}/templates'])
        template = lookup.get_template(self.template_name)

        return Response(template.render(**self.context), self.status)

class QueryBag:
    def __init__(self, query_dict):
        self._query_dict = query_dict
    
    def get(self, name):
        if name in self._query_dict:
            return escape(self._query_dict[name][0])
                    
        return None
