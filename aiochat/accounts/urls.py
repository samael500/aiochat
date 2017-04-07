from accounts import views

routes = (
    dict(method='*', path='/signup', handler=views.SignUp, name='signup'),
    dict(method='*', path='/login', handler=views.LogIn, name='login'),
    dict(method='GET', path='/logout', handler=views.LogOut, name='logout'),
)
