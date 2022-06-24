from flask import Flask

#Creating Flask App
app = Flask(__name__)

#Creating Data Schema
status = ["ON", "OFF"]

#Return current status of signal
@app.route('/', methods=['GET'])
def index():
    return "This is the status of the webpage: "

#Turn status on
@app.route('/activate', methods = ['POST'])
def activate():
    status = ["ON"]
    return "The status was just switched to " + status

#Turn status off
@app.route('/deactivate', methods = ['POST'])
def deactivate():
    status = ["OFF"]
    return "The status was just switched to " + status

if __name__ == "__main__":
    app.run(debug=True)

