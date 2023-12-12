import os

from sqlalchemy import create_engine, text

db_connection_string=os.environ['DB_CONNECTION_STRING']
print(os.environ.get('DB_CONNECTION_STRING'))
engine = create_engine(
 db_connection_string, 
 connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
 })
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._asdict()))
    return jobs 

def load_job_from_db(job_id): 
  with engine.connect() as conn:
    
    result = conn.execute(
      text("select * from jobs where id = :id"), {'id': job_id}) 
    rows = result.all()
    if len(rows) == 0:
      return None
    else: 
      return dict(rows[0]._asdict())

def add_appl_to_db(jobid, full_ame):
 with engine.connect() as conn:
    insert_query = text(
        "INSERT INTO applications (jobid, full_ame) "
        "values (:jobid, :full_ame)"
    )
    conn.execute(insert_query, {'jobid': jobid, 'full_ame': full_ame})
                 