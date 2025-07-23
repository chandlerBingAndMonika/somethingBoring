from mongoengine import Document, StringField, IntField

class Version_Package(Document):
    name = StringField(required=True)
    repo_url = StringField(required=True)
    storage_path = StringField(required=True)
    is_web = StringField(default="False") # האם החבילה היא מהאינטרנט
    version = StringField(required=True)
    isUpdating = bool = False
    web_site = StringField(default="")  # כתובת אתר אם יש

