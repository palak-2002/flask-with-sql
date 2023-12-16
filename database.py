from sqlalchemy import create_engine, text


db_connection_string="mysql+pymysql://8zeeg975j44gydrnztck:pscale_pw_rRxEYSGMS8ibWb3l7tyBPuBncjmNyMPhdrBzvcAfovI@aws.connect.psdb.cloud/jobsnmore?charset=utf8mb4"
engine = create_engine(db_connection_string,
  connect_args={
     "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem" } 
  })



def load_jobs():
  with engine.connect() as conn:
       result=conn.execute(text(
         "select * from job "))

       jobs1=[]
       for row in result.all():
             jobs1.append(row._asdict)
       return jobs1
    
def load_one_job(id):
  with engine.connect() as conn:
       result=conn.execute(
         text("select * from jobs where id=:val"))
       val=id
       rows=result.all()
       if len(rows)==0:
           return None
       else:
           return rows[0]._asdict

# 
#      result=conn.execute(text("select * from jobs"))

  
#      result_dicts=[]
#      for row in result.all():
#            result_dicts.append(row._asdict)
       
# print(result_dicts)
