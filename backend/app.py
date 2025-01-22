from flask import Flask, request, jsonify # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return "IELTS Speaking Test Simulation is running!"

if __name__ == "__main__":
    app.run(debug=True)
