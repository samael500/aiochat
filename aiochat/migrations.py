# Not real migrations, just create tables

from database import objects
from accounts.models import User

with objects.allow_sync():
    User.create_table()
