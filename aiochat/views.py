import aiohttp_jinja2
from aiohttp import web


class Index(web.View):

    """ Main page view """

    template_name = 'index.html'

    @aiohttp_jinja2.template(template_name)
    async def get(self):
        return {}
