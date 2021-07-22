import tkinter as tk
from tkinter import RAISED



def home_interface(self):
    explain_onglet_graph(self)


def explain_onglet_graph(self):
    textWelcome = "👋 Bonjour est bienvenue sur Pymazon, Vous pouvez decouvrir notre interface de gestion regroupant :"
    tk.Label(self, text=textWelcome).place(x=250, y=20,width=750,height=50)


    textOngletGraph = "📊 Onglet Graphique  \n \n Les logs vous permettez de voir les differents \n actions réalisé sur l'application Pymazon \n notament les logs des envoye de mail vis a vis des clients etc.."
    tk.Label(self, text=textOngletGraph).place(x=30, y=160,width=450,height=250)


    textOngletDB =  " 📥 Onglet DB \n \n Les logs vous permettez de voir les differents \nactions réalisé sur l'application Pymazon \n notament les logs des envoye de mail vis a vis des clients etc.."
    tk.Label(self,text=textOngletDB).place(x=700, y=160,width=450,height=250)



    textOngletMail = " 📨 Onglet Mail \n \n Les logs vous permettez de voir les differents \nactions réalisé sur l'application Pymazon  notament \n les logs des envoye de mail vis a vis des clients etc.."

    tk.Label(self, text=textOngletMail).place(x=30, y=450,width=450,height=250)



    textOngletLog = " 🧾 Onglet LOG \n \n Les logs vous permettez de voir les differents \n actions réalisé sur l'application Pymazon notament \n les logs des envoye de mail vis a vis des clients etc.."

    tk.Label(self, text=textOngletLog).place(x=700, y=450, width=450,height=250)
