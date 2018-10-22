from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from CrossSection import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

class HelloWorld(Resource):
    def get(self):
        return {"about":"Hello world"}

class JsonExample(Resource):
    def post(self):
        req_data = request.get_json()
        print(req_data)
        return jsonify(testik(req_data))

api.add_resource(HelloWorld,"/")
api.add_resource(JsonExample,"/json-example")

if __name__ == '__main__':
    app.run(debug=True)
