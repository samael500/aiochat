from aiohttp import web


def json_response(func):
    """ Wrapper for view method, to return JsonResponse """
    async def wrapped(*args, **kwargs):
        content, status = await func(*args, **kwargs)
        return web.json_response(data=content, status=status)
    return wrapped
