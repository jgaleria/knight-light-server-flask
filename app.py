from flask import Flask, jsonify

#Creating Flask App
app = Flask(__name__)

#Creating Data Schema
status = { "status": "OFF" }

#Server
server = { "server": "python flask" }

#Return current status of signal
@app.route('/', methods=['GET'])
def index():
    return jsonify(status, server)

#Turn status on
@app.route('/activate', methods = ['POST'])
def activate():
    status["status"]= "ON"
    return jsonify(status, server)

#Turn status off
@app.route('/deactivate', methods = ['POST'])
def deactivate():
    status["status"]= "OFF"
    return jsonify(status, server)


if __name__ == "__main__":
    app.run(debug=True)

