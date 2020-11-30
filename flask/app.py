from flask import Flask
from flask import escape

app = Flask(__name__)

titre = '<title>HELLO H3</title>'

@app.route("/")
def index():
    return titre + "accueil"
    
@app.route("/hello/<string:username>")
def salutation(username):
    return "Hello %s" % escape(username)

if __name__ == '__main__':
    app.run(debug=True)
