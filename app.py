from flask import Flask, render_template,jsonify
from database import load_jobs,load_one_job



app=Flask(__name__)

# Job=[
#   {
#     "id": 5603,
#     "title":"Data Analyst",
#     "loc": "banglore" ,
#     "sal": "12,00,000",
#     "exp": "minimum 1 year",
#     "mail":"palakjain2002@gmail.com"
#   },
#   {
#     "id": 5610,
#     "title": "Data Scientist",
#     "loc": "delhi",
#     "sal": "15,00,000",
#     "exp": "minimum 2 years",
#     "mail":"palakjain2002@gmail.com"
#   },
#   {
#     "id": 5607,
#     "title": "Associate Software Engineer",
#     "loc": "noida",
#     "sal": "8,00,000",
#     "exp": "none",
#     "mail":"palakjain2002@gmail.com"
#   }
  
# ]



  # print(result_dicts)

  
@app.route("/")
def hello():
  jobs2=load_jobs()
  return render_template("home.html",jobs=jobs2)
@app.route("/job/<id>")
def show_job(id):
  job=load_one_job(id)
  if not job:
    return "Not Found",404
  return render_template("jobpage.html",job=job)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)