from src.models.tag import Tag
from src.services.logger import Logger


def deleteTag(tag):
    Logger("DeleteTag", {
        "subject": "Delete of Tag : " + tag.name ,
    })
    Tag.delete().where(Tag.id == tag.id).execute()

