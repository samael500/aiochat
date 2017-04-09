import peewee
import peewee_async


database = peewee_async.PostgresqlDatabase(None)

class BaseModel(peewee.Model):

    """ Base model with db Meta """

    class Meta:
        database = database
