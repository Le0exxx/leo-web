from flask import Flask

SECRET_KEY = 'you-will-never-guess'
app = Flask(__name__)
app.config.from_object('config')