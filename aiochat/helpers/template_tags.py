
def get_messages(request):
    """ Get messages from session and empty """
    messages = request.session.get('messages', [])
    request.session['messages'] = []
    return messages


tags = {'get_messages': get_messages}
