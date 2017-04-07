import json
import aiohttp_jinja2

from aiohttp import web
from aiohttp_session import get_session
from accounts.models import User

from helpers.shortcuts import redirect
from helpers.decorators import json_response


class Login(web.View):

    """ Simple Login user by username """

    @aiohttp_jinja2.template('accounts/login.html')
    async def get(self):
        print (dir(self.request))
        session = await get_session(self.request)
        if session.get('user'):
            redirect(self.request, 'main')
        return {'conten': 'Please enter login or email'}

    @json_response
    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.check_user()
        if isinstance(result, dict):
            session = await get_session(self.request)
            set_session(session, str(result['_id']), self.request)
        else:
            return web.Response(content_type='application/json', text=convert_json(result))
