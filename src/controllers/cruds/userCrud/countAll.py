from src.models.user import User

def countAllUser():
    return User.select().count()
