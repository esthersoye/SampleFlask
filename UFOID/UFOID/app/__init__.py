#import the package Flask
from flask import Flask

#create an app variable to store the __name__ passed from the Flask class
app = Flask(__name__)

#import routes modules from the app package
from app import routes