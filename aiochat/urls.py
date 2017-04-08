from index.urls import routes as index_roures
from accounts.urls import routes as accounts_routes
from chat.urls import routes as chat_routes


routes = (
    * index_roures,
    * accounts_routes,
    * chat_routes,
)
