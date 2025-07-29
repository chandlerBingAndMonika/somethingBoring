from mongoengine import Document, StringField, IntField, BooleanField

class Version_Packages(Document):
    name = StringField(required=True)
    repo_url = StringField(required=True)
    is_web = BooleanField(default="False") # האם החבילה היא מהאינטרנט
    version = StringField(required=True)
    isUpdating = bool = False
    web_site_to_version = StringField(default="")  # כתובת אתר אם יש
    is_direct = BooleanField(default="False")

