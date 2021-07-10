from tkinter import *
import tkinter as tk
from src.controllers.cruds.userCrud.get import getUser
from src.models.user import User
from src.services.mailSender import MailSender


def mailSenderView(self):
    displayUserList(self)
    displaySubjectAndBodyFields(self)
    displaySendButton(self)

def displayUserList(self):
    Label(self, text="User list").place(x=680, y=10)

    userScrollbar = Scrollbar(self)
    self.users = Listbox(self, width=80, height=31, selectmode="multiple", yscrollcommand=userScrollbar.set)
    userScrollbar.config(command=self.users.yview)
    self.users.place(x=680, y=30)

    i = 0
    for user in getUser(0).order_by(User.firstName):
        self.users.insert(END, [user.firstName, user.lastName, user.mailAddress])
        self.users.itemconfig(i, bg="#eaeaea" if i % 2 == 0 else "#dadada")
        i += 1

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
    MailSender(
        recipients=getSelectedUsers(self),
        subject=self.subjectField.get("1.0", "end-1c"),
        body=self.bodyField.get("1.0", "end-1c")
    )

def getSelectedUsers(self):
    selectedUsers = []
    listbox = self.users.curselection()
    for i in listbox:
        user = self.users.get(i)
        selectedUsers.append(user[2])
    return selectedUsers
