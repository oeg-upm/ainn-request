import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Request as RequestModel
from models import Response as ResponseModel


##############################
#           Request          #
##############################


class Request(MongoengineObjectType):
    class Meta:
        model = RequestModel
        interfaces = (Node, )


class CreateRequest(graphene.Mutation):

    class Arguments:
        requester_id = graphene.String(required=True)
        dataset_id = graphene.String(required=True)
        description = graphene.String(required=True)

    request = graphene.Field(Request)

    def mutate(self, info, **kwargs):
        request = RequestModel(**kwargs)
        request.save()
        return CreateRequest(request=request)


################################
#           Response           #
################################


class Response(MongoengineObjectType):
    class Meta:
        model = ResponseModel
        interfaces = (Node,)


class CreateRequestInput(graphene.InputObjectType):
    requester_id = graphene.String()
    dataset_id = graphene.String()
    description = graphene.String()


class CreateResponse(graphene.Mutation):

    class Arguments:
        mapping_url = graphene.String()
        description = graphene.String()
        responder_id = graphene.String(required=True)
        status = graphene.String()
        request = CreateRequestInput(required=True)
        #geo = CreateRequestInput(required=True)

    response = graphene.Field(Response)
    #Output = Response

    # def mutate(self, info, geo):
    #     return Response(request=geo.latlng)
    # def mutate(self, info, geo, **kwargs):
    #     # request = RequestModel.objects.get(kwargs['request'])
    #     # kwargs['request']=request
    #     request = RequestModel.objects.get(geo)
    #     kwargs['request']=request
    #     response = ResponseModel(**kwargs)
    #     response.save()
    #     return CreateResponse(response=response)

    # def mutate(self, info, **kwargs):
    #     print 'mutate'
    #     print 'kwargs request: '
    #     print kwargs['geo']
    #     req_kw = kwargs['geo']
    #     request_instance = RequestModel.objects.get(**req_kw)
    #     print 'request instance: '
    #     print request_instance
    #     kwargs['request'] = request_instance
    #     del kwargs['geo']
    #     new_response_instance = ResponseModel(**kwargs)
    #     print 'new response instance: '
    #     print new_response_instance
    #     new_response_instance.save()
    #     return CreateResponse(response=new_response_instance)

    def mutate(self, info, **kwargs):
        req_kw = kwargs['request']
        request_instance = RequestModel.objects.get(**req_kw)
        kwargs['request'] = request_instance
        del kwargs['request']
        new_response_instance = ResponseModel(**kwargs)
        print 'new response instance: '
        print new_response_instance
        new_response_instance.save()
        return CreateResponse(response=new_response_instance)


class Query(graphene.ObjectType):
    node = Node.Field()
    request = MongoengineConnectionField(Request)
    response = MongoengineConnectionField(Response)


class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()
    create_response = CreateResponse.Field()


schema = graphene.Schema(query=Query, types=[Request, Response], mutation=Mutation)
