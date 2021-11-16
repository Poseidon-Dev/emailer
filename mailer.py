from email.message import EmailMessage
import smtplib, ssl
from typing import List
import config

class Mailer:

    def __init__(self, recipients: List):
        self.port = config.EMAIL_SMTP_PORT
        self.server = config.EMAIL_SMTP
        self.sender = config.EMAIL_UID
        self.pwd = config.EMAIL_PWD
        self.recipients = recipients
        self.context = ssl.create_default_context()

    
    def msg(self, subject, message):
        msg = EmailMessage()
        msg['From'] = self.sender
        msg['To'] = self.recipients
        msg['Subject'] = subject
        msg.set_content(message, subtype='html')
        return msg

    
    def send_message(self, subject, message, *args, **kwargs):
        try:
            with smtplib.SMTP_SSL(self.server, self.port) as smtp:
                smtp.login(self.sender, self.pwd)
                smtp.send_message(self.msg(subject, message))
                print('message sent')
        except Exception as e:
            print(f'email failed for {e} reason')


    def send_plaintext(self, subject, message):
        try:
            with smtplib.SMTP_SSL(self.server, self.port) as smtp:
                smtp.login(self.sender, self.pwd)
                smtp.send_message(self.msg(subject, message))
        except Exception as e:
            print(f'email failed for {e} reason')



def send_email(subject, message):
    port = config.EMAIL_SMTP_PORT
    smtp_server = config.EMAIL_SMTP
    sender = config.EMAIL_UID
    password = config.EMAIL_PWD
    recipient = ['ecms-file-transfers@arizonapipeline.com']

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(message)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print('Email Message Sent')
    except Exception as e:
        print(f'Email did not send: {e}')