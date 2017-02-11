from functools import wraps
from flask import request, session, current_app as app
from flask.ext import restful

def sanitize_response(response):
    data = None
    status = 200
    headers = {}

    if isinstance(response, tuple):
        if len(response) is 3:
            data, status, headers = response
        elif len(response) is 2:      
            data, status = response
        else:
            data = response
    else:
        data = response

    return (data, status, headers)

def patch_response_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, status, headers = sanitize_response(func(*args, **kwargs))
        patched = isinstance(data, dict) and ( "responseData" in data ) and ("message" in data )

        if not patched:
            data = {
                "responseData": data,
                "message" : "",
                "status"  : True
            }


        return (data, status, headers)
    return wrapper

def cors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, status, headers = sanitize_response(func(*args, **kwargs))

        cors_allow_headers = ', '.join(app.config.get('CORS_ALLOW_HEADERS', []))
        cors_allow_origins = ', '.join(app.config.get('CORS_ALLOW_ORIGINS', []))
        cors_allow_methods = ', '.join(app.config.get('CORS_ALLOW_METHODS', []))

        headers.update({
            'Access-Control-Allow-Headers': cors_allow_headers,
            'Access-Control-Allow-Origin': cors_allow_origins,
            'Access-Control-Allow-Methods': cors_allow_methods
        })

        return (data, status, headers)
    return wrapper


class Resource(restful.Resource):
    def options(self):
        app.logger.info("Obtained options request from %s",
                        request.remote_addr)
        return "OK"
    options.authenticated = False

    method_decorators = [
        patch_response_data
    ]