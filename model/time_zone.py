from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, 
    ReferenceField, 
    StringField,
)

class TimeZone(Document):
    meta = {'collection': 'timezone'}
    location_name = StringField()
    location_zone = StringField()