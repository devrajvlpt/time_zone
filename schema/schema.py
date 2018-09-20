import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model.time_zone import TimeZone as TimeZoneModel


class TimeZoneSchema(MongoengineObjectType):

    class Meta:
        model = TimeZoneModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_timezone = MongoengineConnectionField(TimeZoneSchema)    
    time_zone_query = graphene.Field(TimeZoneSchema)

schema = graphene.Schema(query=Query, types=[TimeZoneSchema])