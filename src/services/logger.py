from datetime import datetime
import json
from json import JSONDecodeError


"""
Logger service :
    - Author : Guillaume Touchet
    - Write an entry in the log file
    - Parameters :
        - action : string, contains the action that called the service
        - data : data transfer object, contains the values to log (see the documentation for more information)
"""
class Logger:
    def __init__(self, action, data):
        self.action = action
        self.data = data
        self.writeLog()

    def writeLog(self):
        try:
            data = json.load(open("./logs.json", "r"))
        except JSONDecodeError:
            with open("./logs.json", "w") as logFile:
                logFile.write("[]")
            data = json.load(open("./logs.json", "r"))
        data.append(self.getLogDto())
        with open("./logs.json", "w") as logFile:
            json.dump(data, logFile, indent=2)

    def getLogDto(self):
        return {
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "action": self.action,
            "data": self.data,
        }
