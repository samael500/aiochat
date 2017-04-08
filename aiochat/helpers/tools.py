from aiohttp import web


def redirect(request, router_name, *, permanent=False):
    """ Redirect to given URL name """
    url = request.app.router[router_name].url()
    if permanent:
        raise web.HTTPMovedPermanently(url)
    raise web.HTTPFound(url)


def add_message(request, kind, message):
    """ Put message into session """
    messages = request.session.get('messages', [])
    messages.append((kind, message))
    request.session['messages'] = messages
