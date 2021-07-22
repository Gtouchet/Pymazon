import tkinter as tk
from tkinter import ttk, END, CENTER
from tkinter.ttk import Label

from src.controllers.cruds.categoryCrud.get import getCategory, getCategoryWithName
from src.controllers.cruds.productCrud.delete import deleteProductWithTagId
from src.controllers.cruds.tagCrud.create import createTag
from src.controllers.cruds.tagCrud.delete import deleteTag
from src.controllers.cruds.tagCrud.get import  getTag

from src.models.tag import Tag
from src.services.logger import Logger


def validateAndCreate(self, categoryName):
    try:
        categorys = getCategoryWithName(categoryName)
        category = categorys[0]
        tag = Tag()
        tag.name = self.nameField.get("1.0", "end-1c")
        tag.category = category.id
        createTag(tag)

    except:
        Logger("ErrorCreateTag", {
            "subject": "Data dosn't match what should be expected",
        })


def displayCreateTag(self):
    Label(self, text="name : ").place(x=100, y=100)
    self.nameField = tk.Text(self, height=1)
    self.nameField.place(x=100, y=120)
    self.nameField.insert(tk.END, "")

    drop_down_menu_Categories(self)

def drop_down_menu_Categories(self):
    categories = []
    for category in getCategory(0):
        categories.append(category.name)

    variable = tk.StringVar(self)
    variable.set(categories[0])

    opt = tk.OptionMenu(self, variable, *categories)
    opt.config(width=10, font=('Helvetica', 12))
    opt.place(x=100, y=200)

    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.place(anchor=CENTER)

    def callback(*args):
        createTagButton = tk.Button(self, text="Create", width=10,
                                        command=lambda: validateAndCreate(self, format(variable.get())))
        createTagButton.place(x=400, y=250)

    variable.trace("w", callback)




def getSelectedTags(self):
    selectedTags = []
    listbox = self.tags.curselection()
    for i in listbox:
        tag = self.tags.get(i)
        selectedTags.append(tag[1])
    return selectedTags


def deleteTags(self):
    for tagId in getSelectedTags(self):
        tag = getTag(tagId)
        deleteProductWithTagId(tag.id)
        deleteTag(tag)
    displayTagListDelete(self)


def displayTagListDelete(self):
    Label(self, text="Tag list").place(x=50, y=320)

    tagsScrollBar = tk.Scrollbar(self)
    self.tags = tk.Listbox(self, width=80, height=20, selectmode="multiple", yscrollcommand=tagsScrollBar.set)
    tagsScrollBar.config(command=self.tags.yview)
    self.tags.place(x=100, y=340)

    i = 0
    for tag in getTag(0).order_by(Tag.name):
        self.tags.insert(END, [tag.name, tag.id])
        self.tags.itemconfig(i, bg="#eaeaea" if i % 2 == 0 else "#dadada")
        i += 1

    deleteTagsButton = tk.Button(self, text="Delete", width=10, command=lambda: deleteTags(self))
    deleteTagsButton.place(x=900, y=600)


def tagFrameShow(self):
    displayCreateTag(self)
    displayTagListDelete(self)
