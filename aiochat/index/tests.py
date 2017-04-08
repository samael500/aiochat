from helpers.test_case import AioChatTestCase, unittest_run_loop


class IndexTestCase(AioChatTestCase):

    """ Testing index app views """

    url_name = 'index'

    def setUp(self):
        super().setUp()
        self.url = self.app.router[self.url_name].url_for()

    @unittest_run_loop
    async def test_url_reversed(self):
        """ Url should be / """
        self.assertEqual(str(self.app.router[self.url_name].url_for()), '/')
        self.assertEqual(str(self.url), '/')

    @unittest_run_loop
    async def test_index(self):
        """ Should get 200 on index page """
        response = await self.client.get('/')
        self.assertEqual(response.status, 200)
        content = await response.text()
        self.assertIn('Simple asyncio chat', content)
