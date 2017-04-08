from chat import views

routes = (
    dict(method='*', path='/chat/rooms', handler=views.ChatRooms, name='create_room'),
    dict(method='GET', path='/chat/rooms/{slug}', handler=views.Room, name='room'),
)
