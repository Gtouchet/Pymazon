import json
from json import JSONDecodeError
from tkinter import *
from tkinter.ttk import *

def statisticsView(self):
    data = readLogFile()
    if data is not None and len(data) != 0:
        displayTotalLogCount(self, data)
        displayDatesCounters(self, data)
        displayActionsCounters(self, data)
    else:
        displayNoLogsLabel(self)
    displayRefreshViewButton(self)

def displayRefreshViewButton(self):
    sendButton = Button(self, text="Refresh statistics", width=25, command=lambda: statisticsView(self))
    sendButton.place(x=10, y=10)

def readLogFile():
    try:
        return json.load(open("./logs.json", "r"))
    except JSONDecodeError:
        pass

def displayTotalLogCount(self, data):
    Label(self, text="Total log counter : " + str(len(data))).place(x=540, y=15)

def displayDatesCounters(self, data):
    values = {}
    for log in data:
        date = log["date"].split(" ")[0]
        if date not in values.keys():
            values[date] = 1
        else:
            values[date] += 1

    dates = Treeview(self, columns=("Date", "Count", "Percent"), height=len(values)*1)
    dates.column("Date", width=80, anchor=W)
    dates.heading("Date", text="Date")
    dates.column("Count", width=50, anchor=CENTER)
    dates.heading("Count", text="Count")
    dates.column("Percent", width=55, anchor=CENTER)
    dates.heading("Percent", text="Percent")
    dates['show'] = 'headings'
    dates.place(x=10, y=50)

    for value in sorted(values):
        dates.insert('', 'end', values=(value.split(" ")[0], str(values[value]), str(round(values[value] / len(data) * 100))+"%"))

def displayActionsCounters(self, data):
    values = {}
    for log in data:
        if log["action"] not in values.keys():
            values[log["action"]] = 1
        else:
            values[log["action"]] += 1

    actions = Treeview(self, columns=("Action", "Count", "Percent"), height=len(values)*1)
    actions.column("Action", width=250, anchor=W)
    actions.heading("Action", text="Action")
    actions.column("Count", width=50, anchor=CENTER)
    actions.heading("Count", text="Count")
    actions.column("Percent", width=55, anchor=CENTER)
    actions.heading("Percent", text="Percent")
    actions['show'] = 'headings'
    actions.place(x=210, y=50)

    for value in sorted(values):
        actions.insert('', 'end', values=(value, str(values[value]), str(round(values[value] / len(data) * 100))+"%"))

def displayNoLogsLabel(self):
    Label(self, text="File logs.json is empty, no statistics to display").place(x=500, y=15)