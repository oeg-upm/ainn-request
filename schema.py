import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Request as RequestModel
from models import Response as ResponseModel


class CreateRequestInput(graphene.InputObjectType):
    # lat = graphene.Float(required=True)
    # lng = graphene.Float(required=True)

    requester_id = graphene.String()
    dataset_id = graphene.String()
    description = graphene.String()


    @property
    def latlng(self):
        # return "({},{})".format(self.lat, self.lng)
        return "({},{},{})".format(self.requester_id, self.dataset_id, self.description)


class Address(graphene.ObjectType):
    latlng = graphene.String()


class CreateAddress(graphene.Mutation):
    class Arguments:
        geo = CreateRequestInput(required=True)

    Output = Address

    def mutate(self, info, geo):
        return Address(latlng=geo.latlng)


class Request(MongoengineObjectType):
    class Meta:
        model = RequestModel
        interfaces = (Node, )


class Response(MongoengineObjectType):
    class Meta:
        model = ResponseModel
        interfaces = (Node,)


# class CreateRequestInput(graphene.InputObjectType):
#     requester_id = graphene.String()
#     dataset_id = graphene.String()
#     description = graphene.String()


class CreateRequest(graphene.Mutation):

    class Arguments:
        requester_id = graphene.String()
        dataset_id = graphene.String()
        description = graphene.String()

    request = graphene.Field(Request)

    def mutate(self, info, **kwargs):
        request = RequestModel(**kwargs)
        request.save()
        return CreateRequest(request=request)


class CreateResponse(graphene.Mutation):

    class Arguments:
        mapping_url = graphene.String()
        description = graphene.String()
        responder_id = graphene.String()
        status = graphene.String()
        #request = CreateRequestInput(required=True)
        geo = CreateRequestInput(required=True)

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
    def mutate(self, info, **kwargs):
        print 'mutate'
        print 'kwargs request: '
        print kwargs['geo']
        req_kw = kwargs['geo']
        request_instance = RequestModel.objects.get(**req_kw)
        print 'request instance: '
        print request_instance
        kwargs['request'] = request_instance
        del kwargs['geo']
        new_response_instance = ResponseModel(**kwargs)
        print 'new response instance: '
        print new_response_instance
        new_response_instance.save()
        return CreateResponse(response=new_response_instance)


class Query(graphene.ObjectType):
    node = Node.Field()
    # all_requests = MongoengineConnectionField(Request)
    # all_responses = MongoengineConnectionField(Response)
    request = MongoengineConnectionField(Request)
    #request = graphene.Field(Request)
    response = MongoengineConnectionField(Response)
    # hello = graphene.String(description='A typical hello world')
    #
    # def resolve_hello(self, info):
    #     return 'World'
    address = graphene.Field(Address, geo=CreateRequestInput(required=True))

    def resolve_address(self, info, geo):
        return Address(latlng=geo.latlng)

    # def resolve_response(self, info, request):
    #     return Response(request=request)



class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()
    create_response = CreateResponse.Field()
    create_address = CreateAddress.Field()


schema = graphene.Schema(query=Query, types=[Request, Response], mutation=Mutation)
