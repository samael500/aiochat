import aiohttp_jinja2
from aiohttp import web
from chat.models import Room


class Index(web.View):

    """ Main page view """

    template_name = 'index.html'

    @aiohttp_jinja2.template(template_name)
    async def get(self):
        if self.request.user:
            return {'chat_rooms': await Room.all_rooms(self.request.app.objects)}
        return {}
