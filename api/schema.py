import graphene
from graphene_django import DjangoObjectType

from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields =  "__all__"

class Query(graphene.ObjectType):
    """
    The first one is BookType, which adapts the Book model to a DjangoObjectType. We set fields to __all__ to indicate that we want all the fields in the model available in our API.
    The Query class defines the GraphQL queries that the API will provide to clients.
    """
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        """
        This method is called to resolve all books query.
        query {
            allBooks {
                id
                title
                author
                yearPublished
                review
            }
        }
        """
        return Book.objects.all()

    def resolve_book(self, info, id):
        """
        This method will request a single book by its id.
        {
        book(id: 1) {
            id
            title
            author
        }
        }
        """
        return Book.objects.get(pk=id)


schema = graphene.Schema(query=Query)




