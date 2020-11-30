from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def index():
    return '<title>HELLO H3</title>'


if __name__ == '__main__':
    app.run(debug=True)
