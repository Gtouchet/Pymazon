from datetime import datetime
import json
from json import JSONDecodeError

class Logger:
    def __init__(self, action, data):
        self.action = action
        self.data = data
        self.writeLog()

    def writeLog(self):
        data = None
        try:
            data = json.load(open("./logs.json", "r"))
        except JSONDecodeError:
            pass
        data.append(self.getLogDto())
        with open("./logs.json", "w") as logsFile:
            json.dump(data, logsFile, indent=2)

    def getLogDto(self):
        return {
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "action": self.action,
            "data": self.data,
        }
