from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Go Tonto!"

if __name__ == "__main__":
    app.run()