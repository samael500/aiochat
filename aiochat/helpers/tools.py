from aiohttp import web
from aiohttp_session import get_session


def redirect(request, router_name, *, permanent=False):
    """ Redirect to given URL name """
    url = request.app.router[router_name].url()
    if permanent:
        raise web.HTTPMovedPermanently(url)
    raise web.HTTPFound(url)


def add_message(request, kind, message):
    """ Put message into session """
    session = await get_session(request)
    if 'messages' not in session:
        session['messages'] = []
    session['messages'].append((kind, message))
