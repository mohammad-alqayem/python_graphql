import graphene
from models.books import Books
from models.genres import Genres
from graphql_demo.types.books.types import BooksType


class BooksQuery:
    books = graphene.List(BooksType)
    books_by_name = graphene.List(BooksType, name=graphene.String())
    books_by_genre = graphene.List(BooksType, name=graphene.String())

    def resolve_books(self, info, **kwargs):
        query = BooksType.get_query(info)
        return query.all()

    def resolve_books_by_name(self, info, **kwargs):
        q = kwargs.get('name')
        books_query = BooksType.get_query(info)

        return books_query.filter(Books.name.contains(q)).all()

    def resolve_books_by_genre(self, info, **kwargs):
        q = kwargs.get('name')

        books_query = BooksType.get_query(info)

        return books_query.join(Genres).filter(Genres.name == q).all()
