from __future__ import print_function
import markovify
import click
import requests

@click.command()
@click.option('--cards', default=1, help='Number of cards to generate')

def invent(cards):

    """
    with open('wordlist.txt') as f:
        text = f.read()
    """

    r = requests.get('https://raw.githubusercontent.com/azend/chains-invent-insanity/master/wordlist.txt')
    text = r.text

    text_model = markovify.Text(text)

    for i in range(cards):
        print(text_model.make_sentence())

if __name__ == '__main__':
    invent()
