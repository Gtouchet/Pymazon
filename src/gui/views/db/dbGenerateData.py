import tkinter as tk
from tkinter import ttk, END
from tkinter.ttk import Label

from src.services.logger import Logger
from src.controllers.cruds.productCrud.countAll import countAllProduct
from src.controllers.cruds.purchaseCrud.countAll import countAllPurchase
from src.controllers.cruds.userCrud.countAll import countAllUser
from src.factory.GenerateData import GenerateData

def displayStatistique(self):
    Label(self, text="Total User : " + str(countAllUser())).place(x=100, y=200)
    Label(self, text="Total Product : " + str(countAllProduct())).place(x=100, y=230)
    Label(self, text="Total Purchase : " + str(countAllPurchase())).place(x=100, y=260)


def generateDatas(self):
    generateData = GenerateData()
    try:
        if (type(int(self.userField.get("1.0", "end-1c"))) == int and type(
                int(self.userField.get("1.0", "end-1c"))) == int and type(
            int(self.userField.get("1.0", "end-1c"))) == int):
            try:
                nbUser = int(self.userField.get("1.0", "end-1c"))
                nbProduct = int(self.productField.get("1.0", "end-1c"))
                nbPurchase = int(self.purchaseField.get("1.0", "end-1c"))
                generateData.generateNewData(nbUser, nbProduct, nbPurchase)
                displayStatistique(self)
            except:
                Logger("ErrorCreate", {
                    "subject": "Erreur while Generating Data in DB View",
                })
    except:
        Logger("ErrorGenerateNotInt", {
            "subject": "Data not of type Int",
        })


def displayGenerateData(self):
    Label(self, text="Number of new User : ").place(x=100, y=400)
    self.userField = tk.Text(self, height=1)
    self.userField.place(x=100, y=420)
    self.userField.insert(tk.END, "")

    Label(self, text="Number of new Product : ").place(x=100, y=450)
    self.productField = tk.Text(self, height=1)
    self.productField.place(x=100, y=480)
    self.productField.insert(tk.END, "")

    Label(self, text="Number of new Purchase : ").place(x=100, y=510)
    self.purchaseField = tk.Text(self, height=1)
    self.purchaseField.place(x=100, y=530)
    self.purchaseField.insert(tk.END, "")

    sendButton = tk.Button(self, text="Create", width=10, command=lambda: generateDatas(self))
    sendButton.place(x=400, y=560)


def statDBFrameShow(self):
    displayStatistique(self)
    displayGenerateData(self)
