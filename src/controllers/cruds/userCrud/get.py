from src.models.user import User


def getUser(id):
    if id == 0:
        return User.get()
    else:
        return User.get_by_id(id)