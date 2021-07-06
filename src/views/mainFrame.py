import tkinter as tk
from src.views.userView import create_widgets

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        create_widgets(self)

def launchApp():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()