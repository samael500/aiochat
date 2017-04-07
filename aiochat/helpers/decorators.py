from aiohttp import web


async def json_response(func):
    async def wrapped(*args, **kwargs):
        content, status = await func(*args, **kwargs)
        return web.json_response(data=content, status=status)
    return wrapped
