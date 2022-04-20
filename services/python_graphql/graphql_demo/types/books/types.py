import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.books import Books


class BooksType(SQLAlchemyObjectType):
    class Meta:
        model = Books
        interfaces = (graphene.relay.Node,)
