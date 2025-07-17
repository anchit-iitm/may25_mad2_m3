from flask_mail import Mail, Message

mail = Mail()


def send_test_email(to, subject, body):
    msg = Message(subject=subject)
    msg.body = body
    msg.html = f"<p>'So this is an test email body'</p>"
    for recipient in to:
        msg.recipients = [recipient]
        mail.send(msg)
    return {"message": "Email sent successfully"}