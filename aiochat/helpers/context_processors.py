from aiohttp_session import get_session


async def messages_processor(request):
    """ Get messages from session and put to context """
    import time
    print (time.time(), 'context in')
    session = await get_session(request)
    messages = session.get('messages', [])
    session['messages'] = []
    print (messages)
    return {'messages': messages}
