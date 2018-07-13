import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Request as RequestModel
from models import Response as ResponseModel


class Request(MongoengineObjectType):
    class Meta:
        model = RequestModel
        intefaces = (Node, )


class Response(MongoengineObjectType):
    class Meta:
        model = ResponseModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_requests = MongoengineConnectionField(Request)
    all_responses = MongoengineConnectionField(Response)


schema = graphene.Schema(query=Query, types=[Request, Response])
