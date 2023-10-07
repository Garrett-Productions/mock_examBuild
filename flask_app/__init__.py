
from flask import Flask
app = Flask(__name__)
#if the name of our app is equal to the main instance of our app, then run
app.secret_key = "ninjasss"