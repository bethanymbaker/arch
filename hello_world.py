from flask import Flask
import inspect

app = Flask(__name__)


@app.route("/")
def mog():
    function_name = inspect.stack()[0][3]
    return f"this function's name is {function_name}"


@app.route("/exodia")
def mog_2():
    return "Vladimir Guerrero"



if __name__ == "__main__":
    app.run(debug=True)