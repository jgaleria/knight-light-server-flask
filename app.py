from flask import Flask

app = Flask(__name__)

@app.route("/")
def status():
    return "This is the status of the webpage: "

@app.route("/activate")
def on():
    return "The status was just switched to ON"

@app.route("/deactivate")
def off():
    return "The status was just switched to OFF"
    