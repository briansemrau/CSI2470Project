#!/usr/bin/env python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.encoders import *
import os

USERNAME = "mkrajcevx74@gmail.com@gmail.com"
PASSWORD = "mwvjfkkedemyqgjx"


def sendMail(to, subject, text, files=[]):
    assert type(to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        if file is str:
            part.set_payload(open(file, "rb").read())
            encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'
                            % os.path.basename(file))
        else:
            part.set_payload(file.read())
            encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'
                            % "file")

        msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=30)
    # server.ehlo_or_helo_if_needed()
    # server.starttls()
    # server.ehlo_or_helo_if_needed()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, to, msg.as_string())
    server.quit()
