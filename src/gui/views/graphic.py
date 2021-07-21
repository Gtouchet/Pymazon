from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from src.controllers.cruds.purchaseCrud.get import getPurchase
from src.controllers.cruds.userCrud.get import getUser

def graphic_interface(self):

    drop_down_menu_graph(self)
    drop_down_menu_Categorie(self)
    drop_down_menu_Tag(self)
    graph_plot3(self)
    grid_info(self)
    zipCodeGraph()


def zipCodeGraph():
    zipCodes = getZipCodesDict(getUser(0))
    for key, value in zipCodes.items():
        print(key, value)


def graph_plot(self):
    self.fig = plt.figure(figsize=(6, 5), dpi=100)
    self.fig.set_size_inches(5, 3)

    # Data to plot
    labels = 'france', 'belgique', 'amsterdam'
    sizes = [50, 25, 25]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'Orange', 'red']
    explode = (0, 0.2, 0)  # explode 1st slice (Ireland), makes it more prominent

    # Plot pie chart
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')  # creates the pie chart like a circle

    canvasRound = FigureCanvasTkAgg(self.fig, master=self)
    canvasRound.draw()
    canvasRound.get_tk_widget().place(relx=0.7, rely=0.3, anchor=CENTER)  # show the barchart on the ouput window

    def closeCanvas():
        canvasRound.delete('ALL')


def graph_plot2(self):
    self.fig2 = plt.figure(figsize=(5, 5), dpi=80)
    labels = ("france", "belgique", "amsterdam")
    labelpos = np.arange(len(labels))
    countrysum = [0, 504, 420]

    ##This section formats the barchart for output

    plt.bar(labelpos, countrysum, align='center', alpha=1.0)
    plt.xticks(labelpos, labels)
    plt.ylabel('Volume')
    plt.xlabel('Country')
    plt.tight_layout(pad=3.2, w_pad=0.5, h_pad=0.1)
    plt.title('Volumes of product sold')
    plt.xticks(rotation=0, horizontalalignment="center")

    # Applies the values on the top of the bar chart
    for index, datapoints in enumerate(countrysum):
        plt.text(x=index, y=datapoints + 0.3, s=f"{datapoints}", fontdict=dict(fontsize=10), ha='center', va='bottom')

    plt.show()

    ## This section draws a canvas to allow the barchart to appear in it
    canvasbar = FigureCanvasTkAgg(self.fig2, master=self)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.7, rely=0.3, anchor=CENTER)




def graph_plot3(self):
    self.fig3 = Figure(figsize=(5, 4), dpi=100)
    t = ["france", "belgique", "amsterdam"]
    s = [0, 504, 420]
    self.fig3.add_subplot(111).plot(t, s)

    canvas = FigureCanvasTkAgg(self.fig3, master=self)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.7, rely=0.3, anchor=CENTER)






def grid_info(self):

    purchases = getPurchase(0)


    # header
    tableau = Treeview(self, columns=('Nom', 'PD', "SD","RD","S","DA","U","P"))
    tableau.column("Nom", width=200, anchor=W)
    tableau.heading('Nom', text='Nom')

    tableau.column("PD", width=200, anchor=W)
    tableau.heading('PD', text="purchaseDate")

    tableau.column("SD", width=200, anchor=W)
    tableau.heading('SD', text="sendingDate")

    tableau.column("RD", width=200, anchor=W)
    tableau.heading('RD', text="receptionDate")

    tableau.column("S", width=50, anchor=W)
    tableau.heading('S', text='status')

    tableau.column("DA", width=200, anchor=W)
    tableau.heading('DA', text="deliveryAddress")

    tableau.column("U", width=50, anchor=W)
    tableau.heading('U', text="user")

    tableau.column("P", width=50, anchor=W)
    tableau.heading('P', text='product')

    tableau['show'] = 'headings'  # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.pack(padx=3, pady=(0, 2))

    # content
    for purch in purchases:
        tableau.insert('', 'end', values=(purch.name, purch.purchaseDate, purch.sendingDate,purch.receptionDate,purch.status,purch.deliveryAddress,purch.user,purch.product))
    tableau.place(relx=0.5, rely=0.80, anchor=CENTER)


def drop_down_menu_graph(self):
    OptionList = [
        "Graph",
        "graph_round",
        "graph_bar",
        "graph_linear"

    ]

    purchases = getPurchase(0)

    variable = tk.StringVar(self)
    variable.set(OptionList[0])



    opt = tk.OptionMenu(self, variable, *OptionList)
    opt.config(width=10, font=('Helvetica', 12))
    opt.place(relx=0.05, rely=0.05, anchor=CENTER)

    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.place(anchor=CENTER)

    def callback(*args):
        if format(variable.get()) == "graph_round":
            graph_plot(self)
            self.fig2.close()
            self.fig3.close()
        elif format(variable.get()) == "graph_bar":
            graph_plot2(self)
            self.fig.close()
            self.fig3.close()
        elif format(variable.get()) == "graph_linear":
            graph_plot3(self)
            self.fig.close()
            self.fig2.close()





    variable.trace("w", callback)


def drop_down_menu_Categorie(self):
    OptionList = [
        "Category",
        "test2",
        "test3",
        "test4"
    ]


    variable = tk.StringVar(self)
    variable.set(OptionList[0])

    opt = tk.OptionMenu(self, variable, *OptionList)
    opt.config(width=10, font=('Helvetica', 12))
    opt.place(relx=0.15, rely=0.05, anchor=CENTER)

    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.place(anchor=CENTER)


def drop_down_menu_Tag(self):
    OptionList = [
        "TAG",
        "test2",
        "test3",
        "test4"
    ]


    variable = tk.StringVar(self)
    variable.set(OptionList[0])

    opt = tk.OptionMenu(self, variable, *OptionList)
    opt.config(width=10, font=('Helvetica', 12))
    opt.place(relx=0.25, rely=0.05, anchor=CENTER)

    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.place(anchor=CENTER)


def getZipCodesDict(users):
    zipCodesDict = {}
    for user in users:
        zipCode = user.address.split("\n")[1][:2]
        if zipCode not in zipCodesDict.keys():
            zipCodesDict[zipCode] = 1
        else:
            zipCodesDict[zipCode] += 1
    return zipCodesDict
