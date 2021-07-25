import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.services.logger import Logger


"""
Mail sender service :
    - Author : Guillaume Touchet
    - Send a mail with a subject and body to a list of recipients
    - Parameters :
        - recipients : list of string, containing all recipient's mail addresses
        - subject : string, contains the subject of the mail to send
        - body : string, contains the body of the mail to send
"""
class MailSender:
    def __init__(self, recipients, subject, body):
        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.sendMail()

        Logger("Mail sent", {
            "subject": self.subject,
            "body": self.body,
            "recipients": self.recipients,
        })

    def sendMail(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("pymazonesgi@gmail.com", "Abcd1234!")
        message = self.createMessage()
        for recipient in self.recipients:
            server.sendmail("PymazonEsgi", recipient, message)
        server.quit()

    def createMessage(self):
        message = MIMEMultipart("alternative")
        message['From'] = "pymazonesgi@gmail.com"
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, "plain"))
        return message.as_string()
