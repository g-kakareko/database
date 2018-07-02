# -*- coding: utf-8 -*-
from flask import Flask
my_app = Flask(__name__) # Create an application object called my_app
import config
my_app.config.from_object(config)
from app import views
# Import the views module from the app package
