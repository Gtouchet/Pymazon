import tkinter as tk
from tkinter import ttk

from src.gui.controllers.home import home_interface
from src.gui.controllers.graphic import graphic_interface
from src.gui.controllers.db import db_interface
from src.gui.views.mailSenderView import mailSenderView

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        master.title("PYMAZON")
        master.geometry("1200x600")
        tab_control = ttk.Notebook(master)

        #init onglet
        home = ttk.Frame(tab_control)
        graphic = ttk.Frame(tab_control)
        DB = ttk.Frame(tab_control)
        mailSender = ttk.Frame(tab_control)

        #Create onglet
        tab_control.add(home, text='Accueil')
        tab_control.add(graphic, text='Graphic')
        tab_control.add(DB, text='DB')
        tab_control.add(mailSender, text='Mail Sender')

        home_interface(home)
        graphic_interface(graphic)
        db_interface(DB)
        mailSenderView(mailSender)

        tab_control.pack(expand=1, fill='both')



def launchApp():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()








