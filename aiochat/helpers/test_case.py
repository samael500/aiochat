from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop  # noqa
from app import create_app


class AioChatTestCase(AioHTTPTestCase):

    """ Base test case for aiochat """

    async def get_application(self, loop):
        """ Return current app """
        serv_generator, handler, app = await create_app(loop)
        return app
