import requests

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
curr = datetime.datetime.now()


def send(email, token):

    SERVER = "smtp.gmail.com"
    PORT = 587
    FROM = "ankitch860@gmail.com"
    TO = email
    PASS = 'shafcdmtabwwzoms'
    msg = MIMEMultipart()
    msg['subject'] = "Verification "
    msg['From'] = FROM
    msg['To'] = TO
    co = "You need to verify your account.Click on http://127.0.0.1:8000/verify/"+token

    msg.attach(MIMEText(co, 'html'))

    print("Creating mail")

    server = SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())
    print('Sending Email')
    server.quit()
    print('Email sent ......')
