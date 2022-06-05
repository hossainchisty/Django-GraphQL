
from django.urls import path
from graphene_django.views import GraphQLView
from . schema import schema

urlpatterns = [
    # Only a single URL to access the GraphQL API.
    path('v1/graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    # URL: http:localhost:8000/api/v1/graphql
]
