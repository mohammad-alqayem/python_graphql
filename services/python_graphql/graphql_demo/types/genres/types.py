import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.genres import Genres


class GenresType(SQLAlchemyObjectType):
    class Meta:
        model = Genres
        interfaces = (graphene.relay.Node,)
