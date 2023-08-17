# We keep the db key access inside the .env so.

import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


load_dotenv()

engine = create_engine(
    os.getenv('db_key'),
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
                'author': row[4],
                'app_link': row[5],
                'github_profile': row[6]
            }
            projects.append(my_dict)
        return projects
    

def load_api_key(title):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM api_keys WHERE title = :title"),{'title':title})
        api_key = result.fetchall()
        if len(api_key) == 0:
            return None
        key = ""
        for i in api_key:
            key = i[2]
        return key
    

def load_project_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM projects WHERE id = :id"), {'id':id})
        result_all = result.fetchall()
        if len(result_all) == 0:
            return None
        projects = []
        for row in result_all:
            my_dict = {
                'id': row[0],
                'title': row[1],
                'location': row[2],
                'birthday': row[3],
                'author': row[4],
                'app_link': row[5],
                'github_profile': row[6]
            }
            projects.append(my_dict)
        return projects