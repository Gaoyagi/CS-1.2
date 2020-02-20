from flask import Flask

from listogram import Listogram
from dictogram import Dictogram

app = Flask(__name__)

@app.route('/')
def index():
    return 'MEMEMEMEMEMEMEMEMEMEMEME'

@app.route('/listogram')
def lists():
    temp = Listogram('one fish two fish red fish blue fish'.split()) 
    return temp.generate_sentence(10)

@app.route('/dictogram')
def Dicts():
    temp = Dictogram('one fish two fish red fish blue fish'.split())  
    return temp.generate_sentence(10)

@app.route('/markov')
def hello_world():
    return 'in progress'