import markovify
import requests


def invent():

    r = requests.get('https://s3.amazonaws.com/chains-invent-insanity/wordlist.txt')
    text = r.text

    text_model = markovify.Text(text)

    for i in range(3):
        return text_model.make_sentence(tries=100)
