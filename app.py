from flask import Flask, jsonify
from flask_pymongo import PyMongo 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/sampledb"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    first_insert = mongo.db.new_collection.find()
    for first in first_insert:
        print first['name']
        return jsonify({"data":first['name']}), 200

if __name__ == '__main__':    
    app.run(port=5002, host= '0.0.0.0', debug=True)

