import tkinter as tk
from tkinter import ttk, END

from src.gui.views.dbCategory import categoryFrameShow
from src.gui.views.dbGenerateData import statDBFrameShow
from src.gui.views.dbProduct import productFrameShow
from src.gui.views.dbTag import tagFrameShow
from src.gui.views.dbUser import userFrameShow


def db_interface(self):
    hi_there = tk.Label(self)
    hi_there["text"] = "Onglet DB"
    hi_there.pack(side="top")

    tab_control = ttk.Notebook(self)

    # init onglet
    statDBFrame = ttk.Frame(tab_control)
    userFrame = ttk.Frame(tab_control)
    productFrame = ttk.Frame(tab_control)
    tagFrame = ttk.Frame(tab_control)
    categoryFrame = ttk.Frame(tab_control)

    # Create onglet
    tab_control.add(statDBFrame, text='Statistics')
    tab_control.add(userFrame, text='user')
    tab_control.add(productFrame, text='Product')
    tab_control.add(tagFrame, text='Tag')
    tab_control.add(categoryFrame, text='Category')

    statDBFrameShow(statDBFrame)
    userFrameShow(userFrame)
    productFrameShow(productFrame)
    tagFrameShow(tagFrame)
    categoryFrameShow(categoryFrame)
    tab_control.pack(expand=1, fill='both')
