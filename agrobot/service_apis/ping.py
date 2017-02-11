from agrobot.utils.resource import Resource


class Ping(Resource):
    def get(self):
        return {'responseData': 'Successful ping status',
                'message': 'Success'}
