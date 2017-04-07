from views import Index
from accounts.views import Login

routes = (
    dict(method='GET', path='/', handler=Index, name='index'),
    dict(method='*', path='/login', handler=Login, name='login'),
)
