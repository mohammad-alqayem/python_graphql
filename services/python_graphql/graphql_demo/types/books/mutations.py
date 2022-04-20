import graphene
from models.books import Books
from database.db_session import db_session
from graphql_demo.types.books.types import BooksType

"""
Books Mutations Inputs
"""


class CreateBookInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    author = graphene.String(required=True)
    genre_id = graphene.Int(required=True)


class DeleteBookInput(graphene.InputObjectType):
    name = graphene.String(required=True)


"""
Books Mutations
"""


class CreateBook(graphene.Mutation):
    book = graphene.Field(lambda: BooksType)
    ok = graphene.Boolean()
    err = graphene.String()

    class Arguments:
        input = CreateBookInput(required=True)

    def mutate(self, info, input):
        book = Books(**input)
        try:
            db_session.add(book)
            db_session.commit()
            return CreateBook(book=book, ok=True, err=None)
        except Exception as e:
            db_session.rollback()
            return CreateBook(book=None, ok=False, err=e.args)


class DeleteBook(graphene.Mutation):
    books = graphene.List(BooksType)
    ok = graphene.Boolean()
    err = graphene.String()

    class Arguments:
        input = DeleteBookInput(required=True)

    def mutate(self, info, input):
        books_query = db_session.query(Books).filter(Books.name == input["name"])
        books = books_query.all()

        if not books:
            return DeleteBook(books=None, ok=False, err=f"No books found with the given name {input['name']}")

        try:
            books_query.delete()
            return DeleteBook(books=books, ok=True, err=None)
        except Exception as e:
            db_session.rollback()
            return DeleteBook(books=None, ok=False, err=e.args)
