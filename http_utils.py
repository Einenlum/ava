from urllib.parse import urlparse, parse_qs
from html import escape

class Request:
    def __init__(self, querystring):
        self._query_bag = QueryBag(parse_qs(querystring))

    @classmethod
    def build_from_wsgi(cls, environ):
        print(environ)
        return Request(environ['QUERY_STRING'])

    @property
    def query(self):
        return self._query_bag

class Response:
    HTTP_OK = '200 OK'
    DEFAULT_CONTENT_TYPE = 'text/html; charset=utf8'

    def __init__(self, status, content):
        self.status = status
        self.content = bytes(content, encoding='utf8')
    
    @property
    def headers(self):
        return [
            ('Content-Type', self.DEFAULT_CONTENT_TYPE),
            ('Content-Length', str(len(self.content)))
        ]

class QueryBag:
    def __init__(self, query_dict):
        self._query_dict = query_dict
    
    def get(self, name):
        if name in self._query_dict:
            return escape(self._query_dict[name][0])
                    
        return None
