import views
from routing import Route


def app():
    routes = [
        Route(r'/', views.hello_pycon),
        Route(r'/article/{article_slug}', views.article),
        Route(r'/articles', views.post_article, {'methods':['POST']})
    ]

    return routes
