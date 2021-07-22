from src.services.logger import Logger


def createTag(tag):
    Logger("CreateTag", {
        "subject": "Create of " + tag.name
    })
    tag.save()