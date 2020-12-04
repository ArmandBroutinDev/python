from flask import Flask
from flask import escape
from flask import render_template
import streamlit as st
import pickle

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/predict")
def predict():
	st.title("TP Streamlit")
    inpt = st.text_input("tweet","")
    s = pickle.dumps(clf)
    clf2 = pickle.loads(s)
    clf2.predict(X[1:2])[0])
    st.text("tweet : {}".format(inpt))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)