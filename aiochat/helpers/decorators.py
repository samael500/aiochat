from aiohttp import web
from helpers.shortcuts import redirect, add_message


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
            add_message('info', 'Sign in to continue.')
            redirect(self.request, 'login')
        return await func(self, *args, **kwargs)
    return wrapped
