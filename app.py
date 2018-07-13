from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from models import Request, Response
from mongoengine import connect


# def init_db():
#     #connect('graphene-mongo-example', alias='default')
#     # req1 = Request(requester_id="123", dataset_id="234", description="this is new", status="open")
#     # req1.save()
#     # req2 = Request(requester_id="029384902842", dataset_id="90328402", description="this is the second", status="close")
#     # res1 = Response(mapping_url="http://www.google.com", description="this is response 1", responder_id="21334",
#     #                 request=req1, status='approved')
#     # req2.save()
#     # res1.save()
#     #Request.objects.delete()


app = Flask(__name__)
app.debug = True


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    connect('graphene-mongo-example', alias='default')
    #init_db()
    app.run()