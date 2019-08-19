from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Beth!"


@app.route("/nabil")
def my_love():
    return "Hello, Nabil!"


if __name__ == "__main__":
    app.run(debug=True)
