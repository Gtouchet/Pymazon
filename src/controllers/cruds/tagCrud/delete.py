from src.controllers.cruds.productCrud.delete import deleteProductWithTagId
from src.models.tag import Tag
from src.services.logger import Logger


def deleteTag(tag):
    Logger("DeleteTag", {
        "subject": "Delete of Tag : " + tag.name ,
    })
    Tag.delete().where(Tag.id == tag.id).execute()

def deleteTagWithCategoryId(id):
    tags = Tag.select().where(Tag.category_id == id).execute()

    for tag in tags:
        deleteProductWithTagId(tag.id)
        deleteTag(tag)
