# Not real migrations, just create tables
import asyncio
from app import create_app

from accounts.models import User
from chat.models import Room, Message

loop = asyncio.get_event_loop()
serv_generator, handler, app = loop.run_until_complete(create_app(loop))

with app.objects.allow_sync():
    User.create_table(True)
    Room.create_table(True)
    Message.create_table(True)

    for room in ('main', 'flood', 'foo', 'bar', 'baz', ):
        try:
            Room.create(name=room)
        except:
            pass

    for user in ('Alice', 'Bob', 'Carol', 'Dave', 'Eve', ):
        try:
            User.create(username=user)
        except:
            pass
