from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data analyst',
    'location': 'Amsterdam',
    'salary': '$200,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'London',

  }
]

@app.route("/")
def hello_world():
    return render_template('Home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0', debug=True)  