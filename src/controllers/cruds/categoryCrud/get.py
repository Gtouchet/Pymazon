from src.models.category import Category


def getCategory(id):
    if id == 0:
        return Category.select()
    if id > 0:
        return Category.get_by_id(id)

