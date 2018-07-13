from mongoengine import Document
from mongoengine.fields import DateTimeField, ReferenceField, StringField, EmailField, URLField
from datetime import datetime


class Request(Document):
    meta = {'collection': 'request'}
    requester_id = StringField()
    dataset_id = StringField()
    description = StringField()
    requested_on = DateTimeField(default=datetime.now)
    STATUSES = (
        ('open', 'Open'),
        ('close', 'Close'),
        ('inprogress', 'In Progress')
    )
    status = StringField(choices=STATUSES, default='open')


class Response(Document):
    meta = {'collection': 'response'}
    mapping_url = StringField(default='')
    description = StringField()
    # responder_email = EmailField()
    responder_id = StringField()
    responded_on = DateTimeField(default=datetime.now)
    request = ReferenceField(Request)
    STATUSES = (
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('new', 'New'),
    )
    status = StringField(choices=STATUSES, default='new')





