from jinja2 import Environment
from aiohttp_session import get_session


async def get_messages(request):
    """ Return and empty messages """
    session = await get_session(request)
    for msg in session.get('messages', []):
        yield msg
    session['messages'] = []


tags = {'get_messages': get_messages, }
