from src.services.logger import Logger


def createCategory(category):
    Logger("CreateCategory", {
        "subject": "Create of " + category.name,
    })
    category.save()


