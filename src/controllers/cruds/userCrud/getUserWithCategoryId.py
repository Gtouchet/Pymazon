from src.controllers.cruds.purchaseCrud.getPurchaseWithCategoryId import getPurchaseWithCategoryId
from src.models.user import User


def getUserWithCategoryId(id):
    purchases = getPurchaseWithCategoryId(id)

    users = []
    for purchase in purchases:
        users.append(User.select().where(User.id == purchase.user.id).execute())
    return users