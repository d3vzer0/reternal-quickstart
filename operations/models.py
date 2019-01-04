from config import config
from generic import Random
import datetime
import mongoengine
import mongoengine as db

db.connect(
    db=config['mongodb']['database'],
    host=config['mongodb']['address'],
    port=int(config['mongodb']['port'])
)

ROLE_OPTIONS = ('user', 'admin')
class Users(db.Document):
    username = db.StringField(max_length=50, required=True, unique=True)
    password = db.StringField(max_length=128, required=True)
    salt = db.StringField(default=Random.create(20), max_length=20, required=True)

    role = db.StringField(max_length=20, required=True, default="user", choices=ROLE_OPTIONS)
    email = db.EmailField(required=True)

    meta = {
        'ordering': ['-username'],
    }

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username


class Commands(db.Document):
    name = db.StringField(max_length=100, required=True, unique=True)
    type = db.StringField(max_length=20, required=True)
    platform = db.ListField(db.StringField(max_length=50, default="all"))


class MitreCommands(db.Document):
    technique_id = db.StringField(max_length=100, required=True, unique=True)
    command = db.StringField(max_length=100, required=True)
    input = db.StringField(max_length=900, required=False)
    idle_time = db.IntField()
    metta_id = db.StringField(max_length=35)


class MitreReferences(db.EmbeddedDocument):
    external_id = db.StringField(max_length=100)
    url = db.StringField(max_length=1000)
    source_name = db.StringField(max_length=100)
    description = db.StringField(max_length=1000)


PLATFORMS = ('Windows', 'Linux', 'All', 'macOS')
class Mitre(db.Document):
    references = db.EmbeddedDocumentListField('MitreReferences')
    platforms = db.ListField(db.StringField(max_length=50, default="all"))
    kill_chain_phases = db.ListField(db.StringField(max_length=100))
    permissions_required = db.ListField(db.StringField(max_length=100))
    technique_id = db.StringField(max_length=100, required=True, unique=True)
    name = db.StringField(max_length=100, required=True)
    description = db.StringField(max_length=9000)
    data_sources = db.ListField(db.StringField(max_length=100))
    detection = db.StringField(max_length=1000)


class RecipeTechniques(db.EmbeddedDocument):
    technique = db.ReferenceField('Mitre')
    idle_time = db.IntField()


class Recipe(db.Document):
    name = db.StringField(max_length=100)
    techniques = db.EmbeddedDocumentListField(RecipeTechniques)
