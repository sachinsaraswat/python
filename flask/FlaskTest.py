from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask API on AWS!"

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/status')
def status():
    return jsonify({"status": "API is running!"})

if __name__ == "__main__":
    app.run(debug=True)

