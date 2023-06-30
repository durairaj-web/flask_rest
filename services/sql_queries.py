import pymysql

from config.dynaconf import settings
from services.logger import logger_error


def get_connection():
    try:
        con = pymysql.connect(host=settings['DATABASE_HOST'], user=settings['DATABASE_UID'],
                              passwd=settings['DATABASE_PWD'], db=settings['DATABASE_NAME'],
                              port=int(settings['DATABASE_PORT']))
        return con
    except Exception as e:
        logger_error(e)


def execute_sql_query(query: str):
    conn = get_connection()
    cur = conn.cursor()
    last_inserted_id = ''
    try:
        cur.execute(query)
        last_inserted_id = cur.lastrowid
        conn.commit()

        return last_inserted_id

    except Exception as e:
        logger_error(e)
        return last_inserted_id

    finally:
        cur.close()
        conn.close()
