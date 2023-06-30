import copy
import os
import sys
from flask import Flask
from flasgger import Swagger, swag_from
from waitress import serve

from config.dynaconf import settings
from constants import exception
from services.logger import logger_error
from services.utils import generate_response
from controller import user


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SWAGGER'] = {
    "url_prefix": "/flask-rest",
    "swagger_version": "2.0",
    "title": "Flask REST",
    "description": """This is a sample flask application.""",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "false"),
    ],
    "specs": [
        {
            "endpoint": 'api-collection',
            "route": '/api-collection'
        }
    ]
}
Swagger(app)


@swag_from(os.path.join("utilities/users", "list.yml"), methods=['GET'])
@app.route('/flask-rest/users', methods=['GET'])
def users_list():
    try:
        resp = user.users_list()
        return resp
    except Exception as e:
        exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger_error(f"Exception at {filename} on {line_number} : {e}")
        r = generate_response(copy.deepcopy(exception.UNHANDLED_EXCEPTION), 500)
        return r


@swag_from(os.path.join("utilities/users", "detail.yml"), methods=['GET'])
@app.route('/flask-rest/users/<int:id>', methods=['GET'])
def users_detail(id):
    try:
        resp = user.users_detail(id)
        return resp
    except Exception as e:
        exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger_error(f"Exception at {filename} on {line_number} : {e}")
        r = generate_response(copy.deepcopy(exception.UNHANDLED_EXCEPTION), 500)
        return r


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=settings['PORT'])