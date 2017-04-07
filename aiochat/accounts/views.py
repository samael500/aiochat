import aiohttp_jinja2
from time import time

from aiohttp import web
from aiohttp_session import get_session

from database import objects
from accounts.models import User
from helpers.tools import redirect, add_message
from helpers.decorators import anonymous_required, login_required


class LogIn(web.View):

    """ Simple Login user by username """

    template_name = 'accounts/login.html'

    @anonymous_required
    @aiohttp_jinja2.template(template_name)
    async def get(self):
        return {}

    @anonymous_required
    async def post(self):
        """ Check username and login """
        data = await self.request.post()
        username = data.get('username', '').lower()
        try:
            user = await objects.get(User, User.username ** username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            await self.login_user(user)
        await add_message(self.request, 'danger', f'User {username} not found')
        redirect(self.request, 'login')

    async def login_user(self, user):
        """ Put user to session and redirect to Index """
        session = await get_session(self.request)
        session['user'] = str(user.id)
        session['time'] = time()
        await add_message(self.request, 'info', f'Hello {user.chat_username}!')
        redirect(self.request, 'index')


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

    template_name = 'accounts/register.html'

    @anonymous_required
    @aiohttp_jinja2.template(template_name)
    async def get(self):
        return {}

    @anonymous_required
    async def post(self):
        """ Check is username unique and create new User """
        data = await self.request.post()
        username = data.get('username', '').lower()
        if await objects.count(User.select().where(User.username ** username)):
            await add_message(self.request, 'danger', f'{username} already exists')
            redirect(self.request, 'register')
        user = await objects.create(User, username=username)
        await self.login_user(user)
