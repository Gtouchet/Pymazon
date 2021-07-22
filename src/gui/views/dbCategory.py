import tkinter as tk
from tkinter import ttk, END
from tkinter.ttk import Label

from src.controllers.cruds.categoryCrud.create import createCategory
from src.controllers.cruds.categoryCrud.delete import deleteCategory
from src.controllers.cruds.categoryCrud.get import getCategory
from src.controllers.cruds.tagCrud.delete import deleteTagWithCategoryId
from src.models.category import Category
from src.services.logger import Logger


def validateAndCreate(self):
    try:

        category = Category()
        category.name = self.nameField.get("1.0", "end-1c")
        createCategory(category)
    except:
        Logger("ErrorCreateCategory", {
            "subject": "Data dosn't match what should be expected",
        })


def displayCreateCategory(self):
    Label(self, text="Name : ").place(x=100, y=100)
    self.nameField = tk.Text(self, height=1)
    self.nameField.place(x=100, y=120)
    self.nameField.insert(tk.END, "")

    createCategoryButton = tk.Button(self, text="Create", width=10, command=lambda: validateAndCreate(self))
    createCategoryButton.place(x=300, y=150)


def getSelectedCategories(self):
    selectedCategories = []
    listbox = self.categories.curselection()
    for i in listbox:
        category = self.categories.get(i)
        selectedCategories.append(category[1])
    return selectedCategories


def deleteCategories(self):
    for categoryId in getSelectedCategories(self):
        category = getCategory(categoryId)
        deleteTagWithCategoryId(categoryId)
        deleteCategory(category)
    displayCategoryListDelete(self)


def displayCategoryListDelete(self):
    Label(self, text="Category list").place(x=50, y=320)

    categoryScrollbar = tk.Scrollbar(self)
    self.categories = tk.Listbox(self, width=80, height=20, selectmode="multiple", yscrollcommand=categoryScrollbar.set)
    categoryScrollbar.config(command=self.categories.yview)
    self.categories.place(x=100, y=340)

    i = 0
    for category in getCategory(0).order_by(Category.name):
        self.categories.insert(END, [category.name, category.id])
        self.categories.itemconfig(i, bg="#eaeaea" if i % 2 == 0 else "#dadada")
        i += 1

    deleteCategoriesButton = tk.Button(self, text="Delete", width=10, command=lambda: deleteCategories(self))
    deleteCategoriesButton.place(x=900, y=600)


def categoryFrameShow(self):
    displayCreateCategory(self)
    displayCategoryListDelete(self)
