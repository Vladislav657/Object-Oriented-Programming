import random
import requests
from wordsgame import BasicWord


def load_random_word(words):
    random_word = random.choice(words)
    return BasicWord(random_word['word'].upper(), random_word['subwords'])


def get_words():
    response = requests.get('https://jsonkeeper.com/b/A9S1')
    return response.json()
