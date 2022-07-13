from flask import Flask, jsonify

#Creating Flask App
app = Flask(__name__)

#Creating Data Schema
status = "OFF"

#Return current status of signal
@app.route('/', methods=['GET'])
def index():
    return jsonify(status)

#Turn status on
@app.route('/activate', methods = ['POST'])
def activate():
    status = "ON"
    return jsonify(status)

#Turn status off
@app.route('/deactivate', methods = ['POST'])
def deactivate():
    status = "OFF"
    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=True)

