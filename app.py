from flask import Flask, jsonify
from flask_pymongo import PyMongo 
from mongoengine import connect
from model.time_zone import TimeZone
from flask_graphql import GraphQLView
from schema.schema import schema


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/sampledb"
mongo = PyMongo(app)

connect('sampledb', host='mongodb://localhost:27017/sampledb', alias='default')

def init_db():
    # Create the fixtures
    timezone = TimeZone(location_name='Sydney', location_zone='PST')
    timezone.save()

@app.route("/")
def home_page():
    first_insert = mongo.db.new_collection.find()
    for first in first_insert:
        print first['name']
        return jsonify({"data":first['name']}), 200


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':      
    app.run(port=5002, host= '0.0.0.0', debug=True)

