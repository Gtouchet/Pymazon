from datetime import datetime
import json
import os

class Logger:
    def __init__(self, action, data):
        self.action = action
        self.data = data
        self.writeLog()

    def writeLog(self):
        with open("./logs.json", "a") as logFile:
            if os.stat("./logs.json").st_size == 0:
                logFile.write("[\n")
            else:
                logFile.seek(logFile.tell() - 1, os.SEEK_SET)
                logFile.truncate()
                logFile.write(",\n")
            logFile.write(json.dumps(self.getLogDto(), indent=4))
            logFile.write("\n]")


    def getLogDto(self):
        return {
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "action": self.action,
            "data": self.data,
        }