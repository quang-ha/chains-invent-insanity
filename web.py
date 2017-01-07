from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
import markovify
import requests
#from libs import invent

app = Flask(__name__)


@app.route("/")
def invent():

    r = requests.get('https://s3.amazonaws.com/chains-invent-insanity/wordlist.txt')
    text = r.text

    text_model = markovify.Text(text)

    for i in range(3):
        return text_model.make_sentence(tries=100)


if __name__ == "__main__":
    app.run()
