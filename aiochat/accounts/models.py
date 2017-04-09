import peewee
from helpers.models import BaseModel


class User(BaseModel):

    """ Simple model for save users in DB """

    username = peewee.CharField(unique=True, index=True, max_length=10, null=False)

    @property
    def chat_username(self):
        return f'@{self.username}'
