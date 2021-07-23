from src.controllers.cruds.purchaseCrud.getPurchaseWithTagId import getPurchaseWithTagId
from src.models.user import User


def getUserWithCategoryId(id):
    purchases = getPurchaseWithTagId(id)

    users = []
    for purchase in purchases:
        users.append(User.select().where(User.id == purchase.user.id).execute())
    return users