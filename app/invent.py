from flask import Flask, render_template, request
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import os
import markovify
import requests

# Tell our app where to get its environment variables from
dotenv_path = join(dirname(__file__), '.env')
try:
    load_dotenv(dotenv_path)
except IOError:
    find_dotenv()

app = Flask(__name__)
app.debug = os.environ.get('DEBUG_MODE')
app.secret_key = os.environ.get('APP_KEY')


def invent(attempts, num_cards):
    """
    :param attempts: Number of attempts markovify should take to generate a valid sentence for each card.
    :param num_cards: Number of cards to generate.
    :return:
    """

    use_local = os.environ.get('USE_LOCAL_WORDLIST')
    attempts_str2int = int(attempts)
    num_cards_str2int = int(num_cards)
    cards = []

    if use_local is True:
        local_wordlist = os.environ.get('LOCAL_WORDLIST')
        text = local_wordlist
    else:
        remote_wordlist = os.environ.get('REMOTE_WORDLIST')
        r = requests.get(remote_wordlist)
        text = r.text

    text_model = markovify.Text(text)

    for i in range(num_cards_str2int):
        cards.append(text_model.make_sentence(tries=attempts_str2int))

    return cards


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        num_cards = request.form['num_cards']
        attempts = request.form['attempts']
        cards = invent(attempts, num_cards)
        return render_template('result.html', cards=cards)

    return render_template('index.html')


app.jinja_env.globals.update(invent=invent)


def main():
    app.run()

if __name__ == "__main__":
    main()
