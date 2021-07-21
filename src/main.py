from pathlib import Path

from src.controllers.createDatabaseTables import createDatabaseTables
from src.factory.GenerateData import GenerateData
from src.gui.mainFrame import launchApp

if __name__ == "__main__":
    generateData = GenerateData()

    if not Path("./pymazon.db").exists():
        open("pymazon.db", "x")
        createDatabaseTables()

        generateData.generateAllData(1000, 500, 1000)

    if not Path("./logs.json").exists():
        open("logs.json", "x")

    launchApp()
