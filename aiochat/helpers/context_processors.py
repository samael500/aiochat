from aiohttp_session import get_session


async def messages_processor(request):
    """ Get messages from session and put to context """
    session = await get_session(request)
    messages = session.get('messages', [])
    session['messages'] = []
    return {'messages': messages}
