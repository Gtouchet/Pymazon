from src.controllers.cruds.userCrud.get import getUser


def mailSenderView(self):
    self.displayUserList()
    self.displaySubjectAndBodyFields()
    self.displaySendButton()

def displayUserList():
    users = getUser(0)
    for user in users:
        pass # create button and display user names and mail address

def displaySubjectAndBodyFields():
    pass

def displaySendButton():
    pass

def sendMail():
    pass