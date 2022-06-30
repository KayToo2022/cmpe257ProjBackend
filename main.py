from random import sample
from flask import Flask, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from api.SamplePath import SamplePath

app = Flask(__name__)
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

class status(Resource):    
    def get(self):
        try:
            return {'data': 'Api running, git enabled'}
        except Exception as e: 
            return {'data': e}

api.add_resource(status, '/')
api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(SamplePath, '/test/sample')