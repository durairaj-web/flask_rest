import json
from flask import make_response
import pandas as pd
from sqlalchemy import create_engine

from config.dynaconf import settings
from constants.sql_queries import LIST_USERS_QUERY, GET_USER_QUERY

engine = create_engine(
            'mysql+pymysql://' + settings['DATABASE_UID']+':' + settings['DATABASE_PWD'] + '@' +
            settings['DATABASE_HOST'] + '/' + settings['DATABASE_NAME']
        )


def generate_response(response, status_code):
    r = make_response(json.dumps(response, indent=4, ensure_ascii=False), status_code)
    r.mimetype = 'application/json'
    return r


def list_users():
    result = pd.read_sql_query(LIST_USERS_QUERY, engine)
    return result


def get_users_detail(user_id):
    result = pd.read_sql_query(GET_USER_QUERY.format(user_id), engine)
    return result


engine.dispose()
