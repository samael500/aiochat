from views import Index

routes = (
    dict(method='GET', path='/', handler=Index, name='index'),
)
