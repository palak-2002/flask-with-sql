from flask import Flask, render_template

app=Flask(__name__)

Job=[
  {
    "id": 5603,
    "title":"Data Analyst",
    "loc": "banglore" ,
    "sal": "12,00,000",
    "exp": "minimum 1 year",
    "mail":"palakjain2002@gmail.com"
  },
  {
    "id": 5610,
    "title": "Data Scientist",
    "loc": "delhi",
    "sal": "15,00,000",
    "exp": "minimum 2 years",
    "mail":"palakjain2002@gmail.com"
  },
  {
    "id": 5607,
    "title": "Associate Software Engineer",
    "loc": "noida",
    "sal": "8,00,000",
    "exp": "none",
    "mail":"palakjain2002@gmail.com"
  }
  
]
@app.route("/")
def hello():
  return render_template("home.html",jobs=Job)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)