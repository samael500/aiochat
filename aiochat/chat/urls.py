from chat import views

routes = (
    dict(method='*', path='/chat/rooms', handler=views.CreateRoom, name='create_room'),
    dict(method='GET', path='/chat/rooms/{slug}', handler=views.ChatRoom, name='room'),
    dict(method='GET', path='/ws/{slug}', handler=views.WebSocket, name='room_ws'),
)
