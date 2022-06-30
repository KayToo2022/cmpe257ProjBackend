from flask_restful import Api, Resource, reqparse

class SamplePath(Resource):
    # Method is defiend through functions

    # We can probably have our model and its functions up here
    # OR we can import our model in case we want to do something else with a get method
    t = 'temp'

    def get(self):
        # parser gets arguments from JSON payload
        parser = reqparse.RequestParser()

        # get arguments
        parser.add_argument('payload', type=str)

        # parse arguments
        args = parser.parse_args()

        # receive argument from parsed arguments
        ret = args['payload']

        # Do stuff in here

        return {
            # response body
            'data': ret,
            'temp': self.t
        }