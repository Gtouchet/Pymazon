import tkinter as tk
from tkinter import ttk, END, CENTER
from tkinter.ttk import Label

from src.controllers.cruds.categoryCrud.create import createCategory
from src.controllers.cruds.categoryCrud.get import getCategory, getCategoryWithName, getCategoryTags
from src.controllers.cruds.productCrud.delete import deleteProduct
from src.controllers.cruds.productCrud.get import getProduct
from src.controllers.cruds.purchaseCrud.delete import deletePurchaseWithProductId
from src.controllers.cruds.tagCrud.get import getTagWithName
from src.models.product import Product
from src.services.logger import Logger


def validateAndCreate(self, category, tagName):
    try:
        tagModel = getTagWithName(tagName)
        tag = tagModel[0]
        product = Product()
        product.name = self.nameField.get("1.0", "end-1c")
        product.price = self.priceField.get("1.0", "end-1c")
        product.category = category
        product.tag = tag.id
        createCategory(product)

    except:
        Logger("ErrorCreateProduct", {
            "subject": "Data dosn't match what should be expected",
        })


def displayCreateProduct(self):
    Label(self, text="name : ").place(x=100, y=100)
    self.nameField = tk.Text(self, height=1)
    self.nameField.place(x=100, y=120)
    self.nameField.insert(tk.END, "")

    Label(self, text="price : ").place(x=100, y=150)
    self.priceField = tk.Text(self, height=1)
    self.priceField.place(x=100, y=180)
    self.priceField.insert(tk.END, "")
    drop_down_menu_Categories(self)

def drop_down_menu_Categories(self):
    categories = []
    for category in getCategory(0):
        categories.append(category.name)

    variable = tk.StringVar(self)
    variable.set(categories[0])

    opt = tk.OptionMenu(self, variable, *categories)
    opt.config(width=10, font=('Helvetica', 12))
    opt.place(x=100, y=220)

    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.place(anchor=CENTER)

    def callback(*args):
        drop_down_menu_Tag(self, format(variable.get()))

    variable.trace("w", callback)

def drop_down_menu_Tag(self, category):
    optionList = []
    categoryModel = getCategoryWithName(category)
    for tag in getCategoryTags(categoryModel[0]):
        optionList.append(tag.name)

    variable = tk.StringVar(self)
    variable.set(optionList[0])

    opt = tk.OptionMenu(self, variable, *optionList)
    opt.config(width=10, font=('Helvetica', 12))
    opt.place(x=250, y=220)

    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.place(anchor=CENTER)

    def callback(*args):
        createProductButton = tk.Button(self, text="Create", width=10,
                                     command=lambda: validateAndCreate(self, categoryModel[0], format(variable.get())))
        createProductButton.place(x=500, y=250)
        return


    variable.trace("w", callback)



def getSelectedProducts(self):
    selectedProducts = []
    listbox = self.products.curselection()
    for i in listbox:
        product = self.products.get(i)
        selectedProducts.append(product[2])
    return selectedProducts


def deleteProducts(self):
    for productId in getSelectedProducts(self):
        product = getProduct(productId)
        deletePurchaseWithProductId(product.id)
        deleteProduct(product)
    displayProductListDelete(self)


def displayProductListDelete(self):
    Label(self, text="Product list").place(x=50, y=320)

    productsScrollBar = tk.Scrollbar(self)
    self.products = tk.Listbox(self, width=80, height=20, selectmode="multiple", yscrollcommand=productsScrollBar.set)
    productsScrollBar.config(command=self.products.yview)
    self.products.place(x=100, y=340)

    i = 0
    for product in getProduct(0).order_by(Product.name):
        self.products.insert(END, [product.name, str(product.price), product.id])
        self.products.itemconfig(i, bg="#eaeaea" if i % 2 == 0 else "#dadada")
        i += 1

    deleteProductsButton = tk.Button(self, text="Delete", width=10, command=lambda: deleteProducts(self))
    deleteProductsButton.place(x=900, y=600)


def productFrameShow(self):
    displayCreateProduct(self)
    displayProductListDelete(self)