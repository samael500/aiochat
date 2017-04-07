from accounts import views

routes = (
    dict(method='*', path='/register', handler=views.Register, name='register'),
    dict(method='*', path='/login', handler=views.LogIn, name='login'),
    dict(method='GET', path='/logout', handler=views.LogOut, name='logout'),
)
