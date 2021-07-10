from tkinter import *
import tkinter as tk
from src.controllers.cruds.userCrud import getUser
from src.services.mailSender import MailSender


def mailSenderView(self):
    displayUserList(self)
    displaySubjectAndBodyFields(self)
    displaySendButton(self)

def displayUserList(self):
    Label(self, text="User list").place(x=700, y=10)

    userScrollbar = Scrollbar(self)
    users = Listbox(self, width=80, height=31, selectmode="multiple", yscrollcommand=userScrollbar.set)
    users.place(x=696, y=30)

    for user in getUser(0):
        users.insert(END, user)

    userScrollbar.config(command=users.yview)

def displaySubjectAndBodyFields(self):
    Label(self, text="Mail subject").place(x=10, y=10)
    self.subjectField = Text(self, height=1)
    self.subjectField.place(x=10, y=30)
    self.subjectField.insert(tk.END, "")

    Label(self, text="Mail body").place(x=10, y=50)
    self.bodyField = Text(self, height=28)
    self.bodyField.place(x=10, y=70)
    self.bodyField.insert(tk.END, "")

def displaySendButton(self):
    sendButton = Button(self, text="Send", width=10, command=lambda: sendMail(self))
    sendButton.place(x=290, y=535)

def sendMail(self):
    print("clicked")
    #MailSender(
    #    recipients="",
    #    subject=self.subjectField.get("1.0", "end-1c"),
    #    body=self.bodyField.get("1.0", "end-1c")
    #)