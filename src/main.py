from pathlib import Path
from src.controllers.fillDatabaseTables import fillDatabaseTables
from src.controllers.createDatabaseTables import createDatabaseTables
from src.views.mainFrame import launchApp

if __name__ == "__main__":

    if not Path("./pymazon.db").exists():
        open("pymazon.db", "x")
        createDatabaseTables()
        fillDatabaseTables()

    if not Path("./logs.txt").exists():
        open("logs.txt", "x")

    launchApp()