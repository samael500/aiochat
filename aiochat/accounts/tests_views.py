from helpers.test_case import AioChatTestCase, unittest_run_loop


class LoginTestCase(AioChatTestCase):

    """ Testing for LoginView """

    url_name = 'login'

    def setUp(self):
        super().setUp()
        self.url = str(self.app.router[self.url_name].url_for())

    @unittest_run_loop
    async def test_url_reversed(self):
        """ Url should be /login """
        self.assertEqual(str(self.app.router[self.url_name].url_for()), '/login')
        self.assertEqual(str(self.url), '/login')

    @unittest_run_loop
    async def test_get_method(self):
        """ Should GET return 200 with login form """
        response = await self.client.get(self.url)
        self.assertEqual(response.status, 200)
        content = await response.text()
        self.assertIn('Please sign in', content)

    @unittest_run_loop
    async def test_user_not_found(self):
        """ Should GET return 302 and msg for not found user """
        response = await self.client.post(self.url, data={'username': 'abcd'}, allow_redirects=False)
        self.assertEqual(response.status, 302)
        self.assertTrue(response.url.endswith(self.url))
        response = await self.client.request('GET', self.url)
        content = await response.text()
        self.assertIn('Please sign in', content)
        self.assertIn('User abcd not found', content)


class RegisterTestCase(AioChatTestCase):

    """ Testing for RegisterView """

    url_name = 'register'

    def setUp(self):
        super().setUp()
        self.url = str(self.app.router[self.url_name].url_for())

    @unittest_run_loop
    async def test_url_reversed(self):
        """ Url should be /register """
        self.assertEqual(str(self.app.router[self.url_name].url_for()), '/register')
        self.assertEqual(str(self.url), '/register')

    @unittest_run_loop
    async def test_get_method(self):
        """ Should GET return 200 with register form """
        response = await self.client.request('GET', self.url)
        self.assertEqual(response.status, 200)
        content = await response.text()
        self.assertIn('Create account', content)
