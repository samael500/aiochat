# Not real migrations, just create tables

from database import objects
from accounts.models import User
from chat.models import Room, Message

with objects.allow_sync():
    User.create_table(True)
    Room.create_table(True)
    Message.create_table(True)
