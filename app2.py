from flask import Flask, render_template, jsonify
from database import load_projects_from_db, load_project_from_db, load_api_key

app2 = Flask(__name__)

@app2.route("/")
@app2.route("/index")
def index():
    unsplash_key = load_api_key('unplash_key')
    return render_template('title.html', unsplash_key = unsplash_key)


@app2.route("/projects")
def me():
    projects = load_projects_from_db()
    return render_template('home.html', projects = projects)


@app2.route("/api/projects")
def list_projects():
    return load_projects_from_db()

@app2.route("/projects/<id>")
def show_project(id):
    projects = load_project_from_db(id)
    return jsonify(projects)



if __name__ == '__main__':
    app2.run(debug = True)



