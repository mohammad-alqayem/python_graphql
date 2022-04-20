import graphene
from graphql_demo.types.characters.types import CharactersType


class CharactersQuery:
    characters = graphene.List(CharactersType)

    def resolve_characters(self, info, **kwargs):
        query = CharactersType.get_query(info)
        return query.all()
