from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Status(db.Model):
#     status = db.Column(db.String(20), primary_key=True, nullable=False)

#     def __repr__(self):
#         return '<Status %r> % self.id'

#Creating Data Schema
# status = ["ON", "OFF"]

#Return current status of signal
@app.route("/")
def index():
    return "This is the status of the webpage: "

#Turn status on
@app.route("/activate", methods = ['PUT'])
def activate():
    return "The status was just switched to ON"

#Turn status off
@app.route("/deactivate", methods = ['PUT'])
def deactivate():
    return "The status was just switched to OFF"

if __name__ == "__main__":
    app.run(debug=True)

