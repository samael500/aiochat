from datetime import datetime

import peewee

from database import database, objects
from accounts.models import User


class Room(peewee.Model):

    """ Chat Room model """

    name = peewee.CharField(unique=True, index=True, max_length=32, null=False)

    class Meta:
        database = database

    @classmethod
    async def all_rooms(cls):
        """ Return all rooms """
        return await objects.execute(cls.select().order_by(cls.name))

    async def all_messages(self):
        """ Filter messages in current room """
        print (self.messages)
        # return await objects.execute(.select().order_by(cls.name))


class Message(peewee.Model):

    """ Chat Message model """

    user = peewee.ForeignKeyField(User, null=True, related_name='messages')
    room = peewee.ForeignKeyField(Room, related_name='messages')
    text = peewee.TextField()
    created_date = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
