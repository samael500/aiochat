from helpers.test_case import AioChatTestCase, unittest_run_loop


class IndexTestCase(AioChatTestCase):

    """ Testing index app views """

    @unittest_run_loop
    async def test_ab(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(1 + 2, 33)

        # request = await self.client.request("GET", "/")
        # assert request.status == 200
        # text = await request.text()
        # assert "Hello, world" in text
