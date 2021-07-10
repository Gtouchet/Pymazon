import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailSender:
    def __init__(self, recipients, subject, body):
        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.sendMail()

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
