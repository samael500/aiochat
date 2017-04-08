
def messages_processor(request):
    """ Get messages from session and put to context """
    messages = request.session.get('messages', [])
    request.session['messages'] = []
    return {'messages': messages}
