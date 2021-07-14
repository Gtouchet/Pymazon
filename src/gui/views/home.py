import tkinter as tk

def home_interface(self):
    hi_there = tk.Label(self)
    hi_there["text"] = "Onglet Accueil"
    hi_there.pack(side="top")

    quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    quit.pack(side="bottom")

