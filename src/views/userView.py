import tkinter as tk

def create_widgets(self):
    hi_there = tk.Button(self)
    hi_there["text"] = "Hello World\n(click me)"
    hi_there["command"] = say_hi
    hi_there.pack(side="top")

    quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    quit.pack(side="bottom")

def say_hi():
    print("hi there, everyone!")
