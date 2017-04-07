from datetime import datetime

import peewee

from database import database
from accounts.models import User


class Room(peewee.Model):

    """ Chat Room model """

    name = peewee.CharField(unique=True, index=True, max_length=32, null=False)

    class Meta:
        database = database


class Message(peewee.Model):

    """ Chat Message model """

    user = peewee.ForeignKeyField(User, null=True, related_name='messages')
    room = peewee.ForeignKeyField(Room, related_name='messages')
    text = peewee.TextField()
    created_date = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
