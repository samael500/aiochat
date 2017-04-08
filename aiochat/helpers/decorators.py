from aiohttp import web
from helpers.tools import redirect, add_message


def json_response(func):
    """ Wrapper for view method, to return JsonResponse """
    async def wrapped(*args, **kwargs):
        content, status = await func(*args, **kwargs)
        return web.json_response(data=content, status=status)
    return wrapped


def login_required(func):
    """ Allow only auth users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is None:
            add_message(self.request, 'info', 'LogIn to continue.')
            redirect(self.request, 'login')
        return await func(self, *args, **kwargs)
    return wrapped


def anonymous_required(func):
    """ Allow only anonymous users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is not None:
            add_message(self.request, 'info', '<a href="/logout" class="alert-link">LogOut</a> to continue.')
            redirect(self.request, 'index')
        return await func(self, *args, **kwargs)
    return wrapped
