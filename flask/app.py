from flask import Flask
from flask import escape
from flask import render_template

app = Flask(__name__)

titre = '<title>HELLO H3</title>'

@app.route("/")
def index():
    #return titre + "accueil"
    return render_template('hello.html')
    
@app.route("/hello/<string:username>")
def salutation(username):
	return render_template('hello.html',name = username)
    #return "Hello %s" % escape(username)

if __name__ == '__main__':
    app.run(debug=True)
