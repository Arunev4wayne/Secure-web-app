from flask import Flask, jsonify, render_template, request

from database import add_appl_to_db, load_job_from_db, load_jobs_from_db

app = Flask(__name__)



@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('Home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = jsonify(load_jobs_from_db())
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)  
  if not job:
    return "Job not found", 404
  return render_template('jobtitle.html', job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
  data = request.form
  # store this in db
  # send an email
  # display an acknowledgment
  job = load_job_from_db(id)
  add_appl_to_db(id, data)
  return render_template('application_submitted.html', job=job, application=data)

if __name__ == "__main__":
  app.run(host='0.0.0', debug=True)  