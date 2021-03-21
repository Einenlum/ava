import views

def app():
    routes = [
        (r'/', views.hello_pycon),
        (r'/article/{article_slug}', views.article)
    ]

    return routes
