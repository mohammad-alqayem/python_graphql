import graphene
from models.genres import Genres
from graphql_demo.types.genres.types import GenresType
from database.db_session import db_session

"""
Genres Mutations Inputs
"""


class CreateGenresInput(graphene.InputObjectType):
    name = graphene.String(required=True)


"""
Genres Mutations 
"""


class CreateGenres(graphene.Mutation):
    genres = graphene.Field(lambda: GenresType)
    ok = graphene.Boolean()
    err = graphene.String()

    class Arguments:
        input = CreateGenresInput(required=True)

    def mutate(self, info, input):
        genres = Genres(**input)
        try:
            db_session.add(genres)
            db_session.commit()
            return CreateGenres(genres=genres, ok=True, err=None)
        except Exception as e:
            db_session.rollback()
            return CreateGenres(genres=None, ok=False, err=e.args)
