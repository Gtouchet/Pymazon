from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.controllers.cruds.productCrud.get import getProduct
from src.controllers.cruds.purchaseCrud.get import getPurchase
from src.controllers.cruds.userCrud.get import getUser
from src.services.logger import Logger


def graphic_interface(self):
    self.graph = None
    self.graphType = None
    self.mainCategory = None
    self.subCategory = None

    displayDropDownMenuGraphChoice(self)
    displayDropDownMenuMainCategoryChoice(self)
    grid_info(self)

def displayGraph(self):
    if self.graphType is None or self.subCategory is None:
        return

    dataToDisplay = getDataToDisplay(self)
    if dataToDisplay is None:
        return

    stats = []
    percents = []
    count = 0
    for key, value in dataToDisplay[0].items():
        if value == 0:
            continue
        if self.subCategory == "Users per region":
            key = key[0] # Use the region's name only
        stats.insert(count, str(key) + " (" + str(value) + ")")
        percents.insert(count, int(value))
        count = +1

    self.graph = plt.figure(figsize=(7, 5), dpi=100)

    if self.graphType == "Pie chart":
        plt.pie(percents, labels=stats, autopct='%1.1f%%')
        plt.axis('equal')

    elif self.graphType == "Bars":
        labelPosition = np.arange(len(stats))
        plt.bar(labelPosition, percents, align='center', alpha=1.0)
        plt.xticks(labelPosition, stats)
        plt.ylabel(dataToDisplay[1])
        plt.xlabel(dataToDisplay[2])
        plt.subplots_adjust(bottom=0.45)
        plt.xticks(rotation=45, ha='right')

    else:
        self.graph.add_subplot(111).plot(stats, percents)
        plt.ylabel(dataToDisplay[1])
        plt.xlabel(dataToDisplay[2])
        plt.subplots_adjust(bottom=0.45)
        plt.xticks(rotation=45, ha='right')

    graph = FigureCanvasTkAgg(self.graph, master=self)
    graph.draw()
    graph.get_tk_widget().place(x=850, y=280, anchor=CENTER)

def getDataToDisplay(self):
    if self.subCategory == "Users per region":
        return getUsersPerRegion(), "Regions", "Users"
    elif self.subCategory == "Products per price range":
        return getProductsPerPriceRange(), "Price ranges", "Products"
    elif self.subCategory == "Products per category":
        return getProductsPerCategory(), "Categories", "Products"
    elif self.subCategory == "Products per tag":
        return getProductsPerTag(), "Tags", "Products"
    elif self.subCategory == "Purchases per year":
        return getPurchasesPerYear(), "Years", "Purchases"
    elif self.subCategory == "Purchases per user":
        return getPurchasesPerUser(), "Users", "Purchases"
    else:
        return None

def displayDropDownMenuGraphChoice(self):
    graphList = [
        "Pie chart",
        "Bars",
        "Linear",
    ]

    choice = tk.StringVar(self)
    choice.set(None)

    dropDownMenu = tk.OptionMenu(self, choice, *graphList)
    dropDownMenu.config(width=10, font=('Helvetica', 12))
    dropDownMenu.place(x=65, y=15, anchor=CENTER)

    def callback(*args):
        self.graphType = format(choice.get())
        displayGraph(self)
    choice.trace("w", callback)

def displayDropDownMenuMainCategoryChoice(self):
    mainCategories = [
        "Users",
        "Products",
        "Purchases",
    ]

    menu = tk.StringVar(self)
    menu.set(None)

    dropDownMenu = tk.OptionMenu(self, menu, *mainCategories)
    dropDownMenu.config(width=10, font=('Helvetica', 12))
    dropDownMenu.place(x=196, y=15, anchor=CENTER)

    def callback(*args):
        self.mainCategory = format(menu.get())
        displayDropDownMenuSubCategoryChoice(self)
    menu.trace("w", callback)

def displayDropDownMenuSubCategoryChoice(self):
    subCategories = ["Users per region"] if self.mainCategory == "Users" \
        else ["Products per price range", "Products per category", "Products per tag"] if self.mainCategory == "Products" \
        else ["Purchases per year", "Purchases per user"]

    menu = tk.StringVar(self)
    menu.set(None)

    subCategoryDropDownMenu = tk.OptionMenu(self, menu, *subCategories)
    subCategoryDropDownMenu.config(width=20, font=('Helvetica', 12))
    subCategoryDropDownMenu.place(x=373, y=15, anchor=CENTER)

    def callback(*args):
        self.subCategory = format(menu.get())
        displayGraph(self)
        displayDownloadFileButton(self)
    menu.trace("w", callback)


def grid_info(self):

    purchases = getPurchase(0)

    ##Dynamisation des donnée grace au dictionnaire

    #for info in dicInfo:
    #    tableau = Treeview(self, columns=(info.surname), height=13)
    #    tableau.column(info.surname, width=200, anchor=W)
    #    tableau.heading(info.surname, text=info.name)
    #    for data in info.data:
    #        tableau.insert('', 'end', values=(data.info.name))
    #    tableau.place(relx=0.5, rely=0.85, anchor=CENTER)

    # header
    tableau = Treeview(self, columns=('Nom', 'PD', "SD","RD","S","DA","U","P"),height=13)
    tableau.column("Nom", width=200, anchor=W)
    tableau.heading('Nom', text='Nom')

    tableau.column("PD", width=200, anchor=W)
    tableau.heading('PD', text="purchaseDate")

    tableau.column("SD", width=200, anchor=W)
    tableau.heading('SD', text="sendingDate")

    tableau.column("RD", width=200, anchor=W)
    tableau.heading('RD', text="receptionDate")

    tableau.column("S", width=50, anchor=W)
    tableau.heading('S', text='status')

    tableau.column("DA", width=200, anchor=W)
    tableau.heading('DA', text="deliveryAddress")

    tableau.column("U", width=50, anchor=W)
    tableau.heading('U', text="user")

    tableau.column("P", width=50, anchor=W)
    tableau.heading('P', text='product')

    tableau['show'] = 'headings'  # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.pack(padx=3, pady=(0, 2))

    # content
    for purch in purchases:
        tableau.insert('', 'end', values=(purch.name, purch.purchaseDate, purch.sendingDate,purch.receptionDate,purch.status,purch.deliveryAddress,purch.user,purch.product))
    tableau.place(relx=0.5, rely=0.85, anchor=CENTER)





def displayDownloadFileButton(self):
    downloadButton = Button(self, text="Download graph", width=20, command=lambda: downloadGraph(self))
    downloadButton.place(x=120, y=260)

def downloadGraph(self):
    filename = self.subCategory + "__" + self.graphType + "__" + datetime.now().strftime("%d-%m-%Y__%Hh%Mm%Ss") + ".png"
    plt.savefig("./downloads/" + filename)
    Logger("Graph downloaded", {
        "statisticDisplayed": self.subCategory,
        "graphType": self.graphType,
        "filename": filename,
    })

def getUsersPerRegion():
    regionDict = {
        ("Bretagne", (29, 22, 56, 35)): 0,
        ("Normandie", (50, 14, 51, 27, 79)): 0,
        ("Nord Pas-de-Calais", (62, 80, 60, 2, 59)): 0,
        ("Ile-de-France", (75, 92, 93, 94, 91, 78, 95, 77)): 0,
        ("Pays de la Loire", (44, 85, 49, 72, 53)): 0,
        ("Centre Val de Loire", (28, 37, 41, 45, 18, 36)): 0,
        ("Aquitaine", (79, 86, 23, 87, 16, 17, 24, 19, 33, 47, 40, 64)): 0,
        ("Languedoc-Roussillon", (65, 32, 31, 9, 11, 66, 81, 82, 46, 12, 48, 30, 34)): 0,
        ("Auvergne", (3, 63, 15, 43, 42, 69, 7, 1, 74, 73, 38, 26)): 0,
        ("Côte d'Azur", (13, 4, 5, 6, 83, 84)): 0,
        ("Bourgogne", (89, 58, 21, 71, 70, 25, 39, 90)): 0,
        ("Alsace", (10, 51, 8, 55, 52, 54, 57, 67, 88, 68)): 0,
    }
    for user in getUser(0):
        zipCode = int(user.address.split("\n")[1][:2])
        for region in regionDict.keys():
            if zipCode in region[1]:
                regionDict[region] += 1
    return regionDict

def getProductsPerPriceRange():
    priceRangeDict = {
        (0, 100): 0,
        (101, 200): 0,
        (201, 300): 0,
        (301, 400): 0,
        (401, 500): 0,
        (501, 600): 0,
        (601, 700): 0,
        (701, 800): 0,
        (801, 900): 0,
        (901, 1000): 0,
        (1001, 2000): 0,
    }
    for product in getProduct(0):
        for key in priceRangeDict.keys():
            if product.price in range(key[0], key[1]):
                priceRangeDict[key] += 1
    return priceRangeDict

def getProductsPerCategory():
    categoriesDict = {}
    for product in getProduct(0):
        if product.category.name not in categoriesDict.keys():
            categoriesDict[product.category.name] = 1
        else:
            categoriesDict[product.category.name] += 1
    return categoriesDict

def getProductsPerTag():
    tagsDict = {}
    for product in getProduct(0):
        if product.tag.name not in tagsDict.keys():
            tagsDict[product.tag.name] = 1
        else:
            tagsDict[product.tag.name] += 1
    return tagsDict

def getPurchasesPerYear():
    yearDict = {}
    for purchase in getPurchase(0):
        purchaseYear = str(purchase.purchaseDate)[:4]
        if purchaseYear not in yearDict.keys():
            yearDict[purchaseYear] = 1
        else:
            yearDict[purchaseYear] += 1
    return yearDict

def getPurchasesPerUser():
    userDict = {}
    for purchase in getPurchase(0):
        user = purchase.user.firstName + " " + purchase.user.lastName
        if user not in userDict.keys():
            userDict[user] = 1
        else:
            userDict[user] += 1
    return userDict


