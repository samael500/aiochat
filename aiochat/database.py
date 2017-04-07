import peewee_async
import settings

database = peewee_async.PostgresqlDatabase(**settings.DATABASE)
database.set_allow_sync(False)
objects = peewee_async.Manager(database)
