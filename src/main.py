from pathlib import Path

from src.controllers.createDatabaseTables import createDatabaseTables
from src.factory.GenerateData import GenerateData
from src.gui.mainFrame import launchApp

if __name__ == "__main__":
    generateData = GenerateData()

    if not Path("./logs.json").exists():
        open("logs.json", "x")

    if not Path("./pymazon.db").exists():
        open("pymazon.db", "x")
        createDatabaseTables()

        generateData.generateAllData(100, 100, 200)

    launchApp()
