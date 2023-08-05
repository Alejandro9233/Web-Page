"""This the database conection"""
import os
from sqlalchemy import create_engine, text

DB = os.environ['KEY_DB']

engine = create_engine(
    DB,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))
        result_all = result.fetchall()
        projects = []
        for row in result_all:
            my_dict = {
                'id': row[0],
                'tittle': row[1],
                'location': row[2],
                'birthday': row[3],
                'author': row[4]
            }
            projects.append(my_dict)
        return projects