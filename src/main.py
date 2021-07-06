from pathlib import Path

from src.controllers.createDb import createDb
from src.controllers.updateDb import updateDb

def main():
    if not Path("./pymazon.db").exists():
        createDb()
    else:
        updateDb()


if __name__ == "__main__":
    main()
