from src.models.category import Category
from src.services.logger import Logger


def deleteCategory(category):
    Logger("DeleteCategory", {
        "subject": "Delete of Category :" + category.name
    })
    Category.delete().where(Category.id == category.id).execute()
