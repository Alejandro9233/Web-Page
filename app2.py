from flask import Flask, render_template
from database import load_projects_from_db

app2 = Flask(__name__)

@app2.route("/")
@app2.route("/index")
def index():
    projects = load_projects_from_db()
    print(projects)
    return render_template('title.html', projects = projects, company_name = 'Alejandro')

@app2.route("/api/projects")
def list_projects():
    return load_projects_from_db()

if __name__ == '__main__':
    app2.run(debug = True)



