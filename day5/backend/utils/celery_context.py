from app import create_app
from celery import Task

app, _ = create_app()

class ContextTask(Task):
    """A Celery Task that runs with Flask application context."""
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)