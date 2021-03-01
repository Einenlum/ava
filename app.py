def my_application(environ, start_response):
    data = b'Hello world'
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])
