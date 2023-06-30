import copy
import json

from flask import make_response
from services.logger import logger_error
from constants import exception, messages
from services.utils import generate_response, list_users, get_users_detail


def users_list():
    try:
        data = list_users()
        print(data)
        resp = copy.deepcopy(messages.VALID_RESPONSE)
        resp['message'] = 'User list fetched successfully'
        resp['data'] = json.loads(data.to_json(orient='records'))
        r = make_response(resp)
        r.mimetype = 'application/json'
        return r
    except Exception as e:
        logger_error(e)
        r = generate_response(copy.deepcopy(exception.UNHANDLED_EXCEPTION), 400)
        return r


def users_detail(id):
    try:
        data = get_users_detail(id)
        if data.empty:
            resp = copy.deepcopy(messages.INVALID_RESPONSE)
            resp['message'] = 'User not found'
            resp['data'] = []
        else:
            resp = copy.deepcopy(messages.VALID_RESPONSE)
            resp['message'] = 'User detail fetched successfully'
            resp['data'] = json.loads(data.to_json(orient='records'))
        r = make_response(resp)
        r.mimetype = 'application/json'
        return r
    except Exception as e:
        logger_error(e)
        r = generate_response(copy.deepcopy(exception.UNHANDLED_EXCEPTION), 400)
        return r
