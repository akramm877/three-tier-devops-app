from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from AWS 3-Tier Application!"


@app.route("/health")
def health():
    return "Application is Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)