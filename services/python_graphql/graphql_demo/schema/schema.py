import graphene
from graphql_demo.schema.query import Query
from graphql_demo.schema.mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
