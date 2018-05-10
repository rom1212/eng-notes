#!/usr/bin/env python

from email.mime.text import MIMEText
import smtplib

def send_email(subject, content):
  email = MIMEText(content)
  sender = 'xxx@xxx.com'
  receivers = ['xxxx@gmail.com','yyyy@gmail.com']
  email['Subject'] = subject
  email['From'] = sender
  email['To'] = ', '.join(receivers)
  server = smtplib.SMTP('localhost')
  server.sendmail(sender, receivers, email.as_string())
