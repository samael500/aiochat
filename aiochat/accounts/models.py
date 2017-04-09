import peewee
from helpers.models import BaseModel


class User(BaseModel):

    """ Simple model for save users in DB """

    username = peewee.CharField(unique=True, index=True, max_length=10, null=False)

    def __str__(self):
        return f'@{self.username}'
