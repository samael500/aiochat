import re
import aiohttp_jinja2

from aiohttp import web, MsgType

from chat.models import Room
from helpers.decorators import login_required
from helpers.tools import redirect, add_message, get_object_or_404


class CreateRoom(web.View):

    """ Create new chat room """

    @login_required
    @aiohttp_jinja2.template('chat/rooms.html')
    async def get(self):
        return {'chat_rooms': await Room.all_rooms(self.request.app.objects)}

    @login_required
    async def post(self):
        """ Check is roomname unique and create new User """
        roomname = await self.is_valid()
        if not roomname:
            redirect(self.request, 'create_room')
        if await self.request.app.objects.count(Room.select().where(Room.name ** roomname)):
            add_message(self.request, 'danger', f'Room with {roomname} already exists.')
            redirect(self.request, 'create_room')
        room = await self.request.app.objects.create(Room, name=roomname)
        redirect(self.request, 'room', parts=dict(slug=room.name))

    async def is_valid(self):
        """ Get roomname from post data, and check is correct """
        data = await self.request.post()
        roomname = data.get('roomname', '').lower()
        if not re.match(r'^[a-z]\w{0,31}$', roomname):
            add_message(self.request, 'warning', (
                'Room name should be alphanumeric, with length [1 .. 32], startswith letter!'))
            return False
        return roomname


class ChatRoom(web.View):

    """ Get room by slug display messages in this Room """

    @login_required
    @aiohttp_jinja2.template('chat/chat.html')
    async def get(self):
        room = await get_object_or_404(self.request, Room, name=self.request.match_info['slug'].lower())
        return {'room': room, 'chat_rooms': await Room.all_rooms(self.request.app.objects), }


class WebSocket(web.View):

    """ Process WS connections """

    async def get(self):
        room = await get_object_or_404(self.request, Room, name=self.request.match_info['slug'].lower())
        user = self.request.user
        app = self.request.app

        app.logger.debug('Prepare WS connection')
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        app.logger.debug('Check current room of WS')
        if room.id not in app.websockets:
            app.websockets[room.id] = []
        app.logger.debug(f'Current ws list of room {app.websockets}')

        app.websockets[self.room.id].append(ws)

        message = await app.objects.create(User, username=username)

        for ws in app.websockets[self.room.id]:
            ws.send_str('message')

        async for msg in ws:
            if msg.tp == MsgType.text:
                if msg.data == 'close':
                    await ws.close()
                else:
                    print (msg.data)
            elif msg.tp == MsgType.error:
                app.logger.debug(f'Connection closed with exception {ws.exception()}')

        # left chat
        app.websockets[self.room.id].remove(ws)
        for ws in app.websockets[self.room.id]:
            ws.send_str('message')
        return ws
