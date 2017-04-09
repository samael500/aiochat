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
        return await objects.execute(cls.select())

    class Meta:
        order_by = ('name', )

    def __str__(self):
        return self.name


class Message(BaseModel):

    """ Chat Message model """

    user = peewee.ForeignKeyField(User, null=True, related_name='messages')
    room = peewee.ForeignKeyField(Room, related_name='messages')
    text = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text

    class Meta:
        order_by = ('created_at', )
