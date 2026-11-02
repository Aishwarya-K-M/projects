from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
from os import path
#from flask_login import LoginManager
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

with open("cyber_bullying_detection/stopwords.txt", "r",encoding='UTF-8') as file:
        stopwords = file.read().splitlines()

vectorizer = TfidfVectorizer(stop_words=stopwords, lowercase=True, vocabulary=pickle.load(open("cyber_bullying_detection/tfidfvectoizer.pkl", "rb")))
model = pickle.load(open("cyber_bullying_detection/voting_classifier.pkl", 'rb'))

from .display import display

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = ''
    app.register_blueprint(display, url_prefix='/')
    return app


