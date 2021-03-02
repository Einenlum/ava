# Ava

A homemade python web framework, just for educational purpose. Obviously, do not use it in production.

Based on [Jacob Kaplan Moss's talk](https://www.youtube.com/watch?v=7kwnjoAJ2HQ).

Work In Progress.

## Installation

```
poetry install
poetry shell
```

Launch the wsgi server on port 8000:

```
APP_PATH=your_module.your_app_function gunicorn -w 4 app:framework_app --reload
```
