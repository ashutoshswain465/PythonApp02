import smtplib
import ssl

host = "smtp.gmail.com"
port = 465


username = "ashutoshswain465@gmail.com"
password = "qspe knfl kufx wtbc"

receiver = "ashutoshswain465@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Email test for python webforms
Hi!
Testing email sent successfully.
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
