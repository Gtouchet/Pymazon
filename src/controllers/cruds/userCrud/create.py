from src.models.user import User
from src.services.logger import Logger


def createUser(user):
    Logger("CreateUser", {
        "subject": "Create of " + user.firstName
    })
    user.save()