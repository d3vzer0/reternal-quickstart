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


PLATFORMS = ('Windows', 'Linux', 'All', 'macOS')
STATUSOPTIONS = ('Processed', 'Open', 'Processing')
TYPEOPTIONS = ('Manual', 'Mitre', 'Actor')
ROLEOPTIONS = ('User', 'Admin')


class Users(db.Document):
    username = db.StringField(max_length=50, required=True, unique=True)
    password = db.StringField(max_length=128, required=True)
    salt = db.StringField(default=Random.create(20), max_length=20, required=True)
    role = db.StringField(max_length=20, required=True, default="User", choices=ROLEOPTIONS)
    email = db.EmailField(required=True)

    meta = {
        'ordering': ['-username'],
    }



class TaskCommands(db.EmbeddedDocument):
    reference = db.StringField(max_length=100, required=False, default=None)
    type = db.StringField(max_length=50, required=True, choices=TYPEOPTIONS)
    name = db.StringField(max_length=150, required=True)
    input = db.StringField(max_length=900, required=False)
    sleep = db.IntField(default=0)


class Commands(db.Document):
    name = db.StringField(max_length=100, required=True, unique=True)
    reference = db.StringField(max_length=100, required=False, default=None)
    type = db.StringField(max_length=20, required=True, choices=TYPEOPTIONS)
    platform = db.ListField(db.StringField(max_length=50, default="all"))


class CommandMapping(db.Document):
    author = db.StringField(max_length=100, required=False)
    name = db.StringField(max_length=100, required=True, unique_with=['technique_id', 'platform', 'kill_chain_phase'])
    description = db.StringField(max_length=200, required=False)
    reference = db.StringField(max_length=100, required=False, default=None)

    technique_id = db.StringField(max_length=200, required=True)
    technique_name = db.StringField(max_length=100, required=True)
    external_id = db.StringField(max_length=100, required=True)
    kill_chain_phase = db.StringField(max_length=100, required=True)
    platform = db.StringField(max_length=30, choices=PLATFORMS, required=True)
    commands = db.EmbeddedDocumentListField('TaskCommands', required=True)


class MitreReferences(db.EmbeddedDocument):
    external_id = db.StringField(max_length=100)
    url = db.StringField(max_length=1000)
    source_name = db.StringField(max_length=100)
    description = db.StringField(max_length=1000)


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
