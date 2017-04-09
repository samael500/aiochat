from aiohttp import web


def redirect(request, router_name, *, permanent=False, **kwargs):
    """ Redirect to given URL name """
    url = request.app.router[router_name].url(**kwargs)
    if permanent:
        raise web.HTTPMovedPermanently(url)
    raise web.HTTPFound(url)


def add_message(request, kind, message):
    """ Put message into session """
    messages = request.session.get('messages', [])
    messages.append((kind, message))
    request.session['messages'] = messages


async def get_object_or_404(request, model, **kwargs):
    """ Get object or raise HttpNotFound """
    try:
        return await request.app.objects.get(model, **kwargs)
    except model.DoesNotExist:
        raise web.HTTPNotFound()
