from flask import Flask
from flask import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/about")
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)