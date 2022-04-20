import graphene
from models.characters import Characters
from graphql_demo.types.characters.types import CharactersType
from database.db_session import db_session

"""
Character Mutations Inputs
"""


class CreateCharacterInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    book_id = graphene.Int(required=True)


"""
Character Mutations 
"""


class CreateCharacter(graphene.Mutation):
    character = graphene.Field(lambda: CharactersType)
    ok = graphene.Boolean()
    err = graphene.String()

    class Arguments:
        input = CreateCharacterInput(required=True)

    def mutate(self, info, input):
        book = Characters(**input)
        try:
            db_session.add(book)
            db_session.commit()
            return CreateCharacter(character=book, ok=True, err=None)
        except Exception as e:
            db_session.rollback()
            return CreateCharacter(character=None, ok=False, err=e.args)
