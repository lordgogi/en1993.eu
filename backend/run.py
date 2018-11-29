from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from CrossSection import *
from Bolts import *

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

class GetBoltOptions(Resource):
    def get(self):
        return jsonify(get_bolt_options())

class GetBoltInlineResults(Resource):
    def post(self):
        bolts=[]
        loads=[]
        req_data = request.get_json()

        for item in req_data['bolts']:
            bolts.append(boltEN(size=req_data['size'], grade=req_data['grade'], x=item['x'], y=item['y']))

        for item in req_data['loads']:
            if item['type'] == 'force':
                loads.append(Force(item['x'],item['y'],item['angle'],item['magnitude']))

        pattern = boltPattern(bolts,loads)
        return jsonify(pattern.return_results())

api.add_resource(HelloWorld,"/")
api.add_resource(JsonExample,"/json-example")
api.add_resource(GetBoltOptions,"/get-bolt-options")
api.add_resource(GetBoltInlineResults,"/get-bolt-inline-result")

#if __name__ == '__main__':
#    app.run(debug=False, ssl_context='adhoc')

if __name__ == '__main__':
    app.run(debug=True)
