import tkinter as tk
from tkinter import ttk, END
from tkinter.ttk import Label

from src.controllers.cruds.purchaseCrud.deletePurchaseWithUserId import deletePurchaseWithUserId
from src.controllers.cruds.userCrud.create import createUser
from src.controllers.cruds.userCrud.delete import deleteUser
from src.controllers.cruds.userCrud.get import getUser
from src.models.user import User
from src.services.logger import Logger


def validateAndCreate(self):
    try:

        user = User()
        user.lastName = self.lastnameField.get("1.0", "end-1c")
        user.firstName = self.firstnameField.get("1.0", "end-1c")
        user.mailAddress = self.mailField.get("1.0", "end-1c")
        createUser(user)
        self.lastnameField.delete(0, END)
        self.firstnameField.delete(0, END)
        self.mailField.delete(0, END)

    except:
        Logger("ErrorCreateUser", {
            "subject": "Data dosn't match what should be expected",
        })


def displayCreateUser(self):
    Label(self, text="firstname : ").place(x=100, y=100)
    self.firstnameField = tk.Text(self, height=1)
    self.firstnameField.place(x=100, y=120)
    self.firstnameField.insert(tk.END, "")

    Label(self, text="lastname : ").place(x=100, y=150)
    self.lastnameField = tk.Text(self, height=1)
    self.lastnameField.place(x=100, y=180)
    self.lastnameField.insert(tk.END, "")

    Label(self, text="mail : ").place(x=100, y=210)
    self.mailField = tk.Text(self, height=1)
    self.mailField.place(x=100, y=230)
    self.mailField.insert(tk.END, "")

    createUserButton = tk.Button(self, text="Create", width=10, command=lambda: validateAndCreate(self))
    createUserButton.place(x=400, y=260)


def getSelectedUsers(self):
    selectedUsers = []
    listbox = self.users.curselection()
    for i in listbox:
        user = self.users.get(i)
        selectedUsers.append(user[2])
    return selectedUsers


def deleteUsers(self):
    for userId in getSelectedUsers(self):
        user = getUser(userId)
        deletePurchaseWithUserId(user.id)
        deleteUser(user)
    displayUserListDelete(self)


def displayUserListDelete(self):
    Label(self, text="User list").place(x=50, y=320)

    userScrollbar = tk.Scrollbar(self)
    self.users = tk.Listbox(self, width=80, height=20, selectmode="multiple", yscrollcommand=userScrollbar.set)
    userScrollbar.config(command=self.users.yview)
    self.users.place(x=100, y=340)

    i = 0
    for user in getUser(0).order_by(User.firstName):
        self.users.insert(END, [user.firstName, user.lastName, user.id])
        self.users.itemconfig(i, bg="#eaeaea" if i % 2 == 0 else "#dadada")
        i += 1

    deleteUsersButton = tk.Button(self, text="Delete", width=10, command=lambda: deleteUsers(self))
    deleteUsersButton.place(x=900, y=600)


def userFrameShow(self):
    displayCreateUser(self)
    displayUserListDelete(self)