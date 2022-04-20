import graphene
from graphql_demo.types.genres.types import GenresType


class GenresQuery:
    genres = graphene.List(GenresType)

    def resolve_genres(self, info, **kwargs):
        query = GenresType.get_query(info)
        return query.all()
