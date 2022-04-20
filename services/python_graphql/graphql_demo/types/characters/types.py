import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.characters import Characters


class CharactersType(SQLAlchemyObjectType):
    class Meta:
        model = Characters
        interfaces = (graphene.relay.Node,)
