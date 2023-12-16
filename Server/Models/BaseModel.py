from ormar import Model
from databases import Database
from sqlalchemy import MetaData

database = Database("sqlite:///Data/Contratos.sqlite")
metadata = MetaData()


class BaseModel(Model):
    class Meta:
        abstract = True
        database = database
        metadata = metadata
