from celery import Celery
from app import create_app
from config import celeryConfig

app, _ = create_app()

def make_celery(init_app):
    init_celery = Celery(init_app.import_name)
    init_celery.config_from_object(celeryConfig)
    return init_celery

celery_app = make_celery(app)

from utils import celery_tasks
from celery.schedules import crontab
celery_app.conf.beat_schedule = {
    'print-hello-every-10-seconds': {
        'task': 'utils.celery_tasks.printHello',
        'schedule': 10.0,
    },
    'query-db-specific-time-daily': {
        'task': 'utils.celery_tasks.query_db',
        'schedule': crontab(hour=10, minute=43),  # Runs daily at 10:43 AM
        'args': (1,)  # Example argument, adjust as needed
    },
    'send-email-monthly': {
        'task': 'utils.celery_tasks.send_email',
        'schedule': crontab(day_of_month='17', hour=10, minute=46),  # Runs on the 17th day of every month at 10:45 AM
    }
}