from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, FlyRank!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok", "service": "my-first-api"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)