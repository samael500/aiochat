import json
import aiohttp_jinja2

from aiohttp import web
from aiohttp_session import get_session

from database import objects
from accounts.models import User
from helpers.tools import redirect, add_message
from helpers.decorators import anonymous_required, login_required


class LogIn(web.View):

    """ Simple Login user by username """

    @anonymous_required
    @aiohttp_jinja2.template('accounts/login.html')
    async def get(self):
        return {}

    @anonymous_required
    @aiohttp_jinja2.template('accounts/login.html')
    async def post(self):
        import time
        print (time.time(), 'view in')

        data = await self.request.post()
        username = data.get('username', '').lower()
        try:
            user = await objects.get(User, username=username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            session = await get_session(self.request)
            session['user'] = str(user.pk)
            session['time'] = time()
            redirect(self.request, 'index')
        await add_message(self.request, 'danger', f'User @{username} not found')
        print (await get_session(self.request))
        return {}


class LogOut(web.View):

    """ Remove current user from session """

    @login_required
    async def get(self):
        session = await get_session(self.request)
        session.pop('user')
        await add_message(self.request, 'info', f'You are logged out')
        redirect(self.request, 'index')


class Register(LogIn):

    """ Remove current user from session """

    @anonymous_required
    @aiohttp_jinja2.template('accounts/register.html')
    async def get(self):
        return {}

    @anonymous_required
    @aiohttp_jinja2.template('accounts/register.html')
    async def post(self):
        data = await self.request.post()
        username = data.get('username', '').lower()
        try:
            user = await objects.get(User, username=username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            session = await get_session(self.request)
            session['user'] = str(user.pk)
            session['time'] = time()
            redirect(self.request, 'index')
        await add_message(self.request, 'danger', f'User @{username} not found')
        return {}
