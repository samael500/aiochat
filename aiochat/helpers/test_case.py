from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
from app import create_app


class AioChatTestCase(AioHTTPTestCase):

    """ Base test case for aiochat """

    async def get_application(self, loop):
        """ Return current app """
        serv_generator, handler, app = await create_app(loop)
        return app


    # async def test_example(self):
    #     request = await self.client.request("GET", "/")
    #     assert request.status == 200
    #     text = await request.text()
    #     assert "Hello, world" in text
