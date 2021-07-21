import tkinter as tk
from tkinter import RAISED



def home_interface(self):
    explain_onglet_graph(self)


def explain_onglet_graph(self):
    textWelcome = "Bonjour est bienvenue sur Pymazon, Vous pouvez decouvrir notre interface de gestion"
    tk.Label(self, text=textWelcome).place(x=200, y=20,width=50,height=150)



    textPresentation = "Notre interface posséde de nombreuses fonctionnalités"
    tk.Label(self, text=textPresentation).place(x=40, y=200)

    textOngletGraph = "Onglet Graphique\n Les logs vous permettez de voir les differents actions réalisé sur l'application Pymazon \n notament les logs des envoye de mail vis a vis des clients etc.."
    tk.Label(self, text=textOngletGraph).place(x=400, y=10,width=450,height=250)


    textOngletDB =  "Onglet DB \n Les logs vous permettez de voir les differents actions réalisé sur l'application Pymazon \n notament les logs des envoye de mail vis a vis des clients etc.."
    tk.Label(self,text=textOngletDB).place(x=30, y=200,width=450,height=250)



    textOngletMail = "Onglet Mail\n Les logs vous permettez de voir les differents \nactions réalisé sur l'application Pymazon  notament \n les logs des envoye de mail vis a vis des clients etc.."

    tk.Label(self, text=textOngletMail).place(x=200, y=200,width=450,height=250)



    textOngletLog = "Onglet LOG \n \n Les logs vous permettez de voir les differents \n actions réalisé sur l'application Pymazon notament \n les logs des envoye de mail vis a vis des clients etc.."

    tk.Label(self, text=textOngletLog).place(x=650, y=400, width=450,height=250)
