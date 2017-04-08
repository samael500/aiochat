from views import Index
from accounts.urls import routes as accounts_routes
from chat.urls import routes as chat_routes


routes = (
    dict(method='GET', path='/', handler=Index, name='index'),
    * accounts_routes,
    * chat_routes,
) 
