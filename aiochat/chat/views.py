import re
import aiohttp_jinja2

from aiohttp import web, MsgType

from chat.models import Room, Message
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
        return {
            'room': room, 'chat_rooms': await Room.all_rooms(self.request.app.objects),
            'room_messages': await room.all_messages(self.request.app.objects)}


class WebSocket(web.View):

    """ Process WS connections """

    async def get(self):
        room = await get_object_or_404(self.request, Room, name=self.request.match_info['slug'].lower())
        user = self.request.user
        app = self.request.app

        def broadcast(message):
            for peer in app.wslist[room.id]:
                peer.send_json(message.as_dict())

        app.logger.debug('Prepare WS connection')
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        app.logger.debug('Check current room of WS')
        if room.id not in app.wslist:
            app.wslist[room.id] = []
        app.logger.debug(f'Current ws list of room {app.wslist}')

        message = await app.objects.create(Message, room=room, user=None, text=f'@{user.username} join chat room')
        app.wslist[room.id].append(ws)
        broadcast(message)

        async for msg in ws:
            if msg.tp == MsgType.text:
                if msg.data == 'close':
                    await ws.close()
                else:
                    message = await app.objects.create(Message, room=room, user=user, text=msg.data)
                    broadcast(message)
            elif msg.tp == MsgType.error:
                app.logger.debug(f'Connection closed with exception {ws.exception()}')

        # left chat
        message = await app.objects.create(Message, room=room, user=None, text=f'@{user.username} left chat room')
        app.wslist[self.room.id].remove(ws)
        broadcast(message)
        return ws
