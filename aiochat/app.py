import asyncio
import aioredis
import jinja2

import aiohttp_jinja2
import aiohttp_debugtoolbar

from aiohttp import web
from aiohttp_session import session_middleware
from aiohttp_session.redis_storage import RedisStorage

from routes import routes
import settings
from settings import logger


async def create_app(loop):
    """ Prepare application """
    redis_pool = await aioredis.create_redis(settings.REDIS_CON, loop=loop)
    middlewares = [session_middleware(RedisStorage(redis_pool))]
    if settings.DEBUG:
        middlewares.append(aiohttp_debugtoolbar.middleware)

    app = web.Application(loop=loop, middlewares=middlewares)
    app['websockets'] = []

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIR))

    if settings.DEBUG:
        aiohttp_debugtoolbar.setup(app)

    # make routes
    for route in routes:
        app.router.add_route(**route)
    app.router.add_static('/static', settings.STATIC_DIR, name='static')

    handler = app.make_handler()
    serv_generator = loop.create_server(handler, settings.HOST, settings.PORT)
    return serv_generator, handler, app


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    serv_generator, handler, app = loop.run_until_complete(create_app(loop))
    server = loop.run_until_complete(serv_generator)

    logger.debug(f'Start server {server.sockets[0].getsockname()}')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        logger.debug('Key pressStop server begin')
    finally:
        loop.run_until_complete(shutdown(serv, app, handler))
        loop.close()
    logger.debug('Stop server end')
