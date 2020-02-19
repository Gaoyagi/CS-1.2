from flask import Flask

from listogram import Listogram
from dictogram import Dictogram

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/listogram')
def lists():
    fish_text = 'one fish two fish red fish blue fish'
    return Listogram(fish_text)  

@app.route('/dictogram')
def Dicts():
    fish_text = 'one fish two fish red fish blue fish'
    return Dictogram(fish_text)

@app.route('/markov')
def hello_world():
    return 'in progress'