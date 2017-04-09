import peewee
from datetime import datetime

from accounts.models import User
from helpers.models import BaseModel


class Room(BaseModel):

    """ Chat Room model """

    name = peewee.CharField(unique=True, index=True, max_length=32, null=False)

    @classmethod
    async def all_rooms(cls, objects):
        """ Return all rooms """
        return await objects.execute(cls.select().order_by(cls.name))

    async def all_messages(self, objects):
        """ Filter messages in current room """
        return await objects.execute(self.messages.order_by(Message.created_at))


class Message(BaseModel):

    """ Chat Message model """

    user = peewee.ForeignKeyField(User, null=True, related_name='messages')
    room = peewee.ForeignKeyField(Room, related_name='messages')
    text = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.now)
