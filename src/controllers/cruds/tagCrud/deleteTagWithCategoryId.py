from src.controllers.cruds.productCrud.deleteProductWithTagId import deleteProductWithTagId
from src.controllers.cruds.tagCrud.delete import deleteTag
from src.models.tag import Tag


def deleteTagWithCategoryId(id):
    tags = Tag.select().where(Tag.category_id == id).execute()

    for tag in tags:
        deleteProductWithTagId(tag.id)
        deleteTag(tag)