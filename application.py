from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
     return '<h1><center>Welcom to Flask application!</center></h1>'