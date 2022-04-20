from graphql_demo.types.books.mutations import *
from graphql_demo.types.genres.mutations import *
from graphql_demo.types.characters.mutations import *


class Mutation(graphene.ObjectType):
    createBook = CreateBook.Field()
    deleteBook = DeleteBook.Field()
    createGenres = CreateGenres.Field()
    createCharacter = CreateCharacter.Field()
