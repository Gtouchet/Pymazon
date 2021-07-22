from src.models.category import Category
from src.models.tag import Tag


def getCategory(id):
    if id == 0:
        return Category.select()
    if id > 0:
        return Category.get_by_id(id)

def getCategoryTags(category):
    return Tag.select().where(Tag.category == category).execute()

def getCategoryWithName(name):
    return Category.select().where(Category.name == name).execute()
