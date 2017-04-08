import aiohttp_jinja2

from aiohttp import web, MsgType

from chat.models import Room, Message
from helpers.decorators import login_required
from database import objects


class ChatRooms(web.View):

    """ Get list of all rooms, and create new """

    @login_required
    @aiohttp_jinja2.template('chat/rooms.html')
    async def get(self):
        rooms = await objects.execute(Room.select().order_by(Room.name))
        return {'rooms': rooms}

    @login_required
    async def post(self):
        """ Check is roomname unique and create new User """
        roomname = await self.is_valid()
        if not roomname:
            redirect(self.request, 'rooms')
        if await objects.count(User.select().where(User.roomname ** roomname)):
            add_message(self.request, 'danger', f'{roomname} already exists')
            redirect(self.request, 'register')
        user = await objects.create(User, roomname=roomname)
        await self.login_user(user)

    async def is_valid(self):
        """ Get roomname from post data, and check is correct """
        data = await self.request.post()
        roomname = data.get('roomname', '').lower()
        if not re.match(r'^[a-z]\w{0,31}$', roomname):
            add_message(self.request, 'warning', (
                'Room name should be alphanumeric, with length [1 .. 32], startswith letter!'))
            return False
        return roomname
