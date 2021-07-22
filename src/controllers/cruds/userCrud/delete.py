from src.models.purchase import Purchase
from src.models.user import User
from src.services.logger import Logger


def deleteUser(user):
    Logger("DeleteUser", {
        "subject": "Delete of user :" + user.firstName
    })
    User.delete().where(User.id == user.id).execute()
