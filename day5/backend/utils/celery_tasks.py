from utils.celery_worker import celery_app
from utils.celery_context import ContextTask

celery_app.Task = ContextTask

@celery_app.task()
def printHello():
    print("Hello from Celery Task")
    from time import sleep
    sleep(5)
    return "celery task executed successfully"

@celery_app.task()
def add(x, y):
    return x + y

@celery_app.task()
def query_db(a):
    from models import Category
    data = Category.query.filter_by(id=a).first()
    if not data:
        return "No category found"
    return data.serialize()

@celery_app.task()
def send_email():
    from utils.mailer import mail
    from models import User
    users = User.query.all()
    from flask_mail import Message
    msg = Message(subject='Test Email')
    msg.body = 'This is a test email from Celery task.'
    for user in users:
        msg.recipients= [user.email]
        mail.send(msg)
    return "Email sent to all users"