from src.models.user import User


def getUser(id):
    if id == 0:
        return User.select()
    else:
        return User.get_by_id(id)


