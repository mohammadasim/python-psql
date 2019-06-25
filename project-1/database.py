from psycopg2 import pool
from sqlalchemy import create_engine


def get_connection(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    return create_engine(url)


#db = get_connection('postgres', 'password123', 'app')
