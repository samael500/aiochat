from chat import views

routes = (
    dict(method='*', path='/chat/rooms', handler=views.ChatRooms, name='rooms'),
)
