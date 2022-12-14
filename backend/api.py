from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

text = {
    "texto": ""
}

@app.route("/")
def toList():
    return jsonify(text), 200


@app.route("/", methods=["POST"])
def toCreate():
    rs = request.json
    text.update({"texto": rs["texto"].upper()})
    return rs, 200


if __name__ == "__main__":
    app.run(host="localhost", port=5005, debug=True)