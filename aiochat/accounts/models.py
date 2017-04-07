import peewee
from database import database


class User(peewee.Model):

    """ Simple model for save users in DB """

    username = peewee.CharField(unique=True, index=True, max_length=10, null=False)

    class Meta:
        database = database

    @property
    def chat_username(self):
        return f'@{self.username}'
