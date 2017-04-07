import json
import aiohttp_jinja2

from aiohttp import web
from aiohttp_session import get_session

from database import objects
from accounts.models import User
from helpers.tools import redirect, add_message



class LogIn(web.View):

    """ Simple Login user by username """

    @anonymous_required
    @aiohttp_jinja2.template('accounts/login.html')
    async def get(self):
        return {}

    @anonymous_required
    @aiohttp_jinja2.template('accounts/login.html')
    async def post(self):
        data = await self.request.post()
        username = data.get('username', '').lower()
        try:
            user = await objects.get(User, username=username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            session = await get_session(self.request)
            session['user'] = str(user_id)
            session['time'] = time()
            redirect(self.request, 'index')
        add_message('danger', f'User "@{username}" not found')
        return {}


class LogOut(web.View):

    """ Remove current user from session """

    async def get(self):
        session = await get_session(self.request)
        session.pop('user')
        redirect(self.request, 'index')


class Register(LogIn):

    """ Remove current user from session """

    async def get(self):
        session = await get_session(self.request)
        session.pop('user')
        redirect(self.request, 'index')
