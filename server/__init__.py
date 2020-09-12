import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from schema.query import Query
from schema.mutation import Mutation


server = FastAPI()

server.add_route(
    "/", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))
