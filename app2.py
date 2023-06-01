from flask import Flask, render_template, jsonify
#import os

app2 = Flask(__name__)

projects = [
    {'id': 1, 'name': 'Virtual Calculator','date':  '2023' },
    {'id': 2, 'name': 'App Tec','date':  '2023'},
    {'id': 3,'name': 'Paint','date':  '2022'}
]

@app2.route("/")
@app2.route("/index")
def index():
    #return os.system("shutdown /s /t 1")
    return render_template('home.html', projects = projects, company_name = 'Alejandro')

@app2.route("/api/jobs")
def list_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app2.run(debug = True)



