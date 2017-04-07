from aiohttp import web
from aiohttp_session import get_session


def redirect(request, router_name, *, permanent=False):
    """ Redirect to given URL name """
    url = request.app.router[router_name].url()
    if permanent:
        raise web.HTTPMovedPermanently(url)
    raise web.HTTPFound(url)


async def add_message(request, kind, message):
    """ Put message into session """
    session = await get_session(request)
    messages = session.get('messages', [])
    messages.append((kind, message))
    session['messages'] = messages
