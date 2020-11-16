from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "I SELL CLOTHES"


@app.route("/home")
def home():
    return "LEE'S HOME WEBSITE"


if __name__ == '__main__':
    app.run(debug=True)


