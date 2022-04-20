import graphene
from graphql_demo.types.books.query import BooksQuery
from graphql_demo.types.genres.query import GenresQuery
from graphql_demo.types.characters.query import CharactersQuery


class Query(graphene.ObjectType, BooksQuery, GenresQuery, CharactersQuery):
    node = graphene.relay.Node.Field()
