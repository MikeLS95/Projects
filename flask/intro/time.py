from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def current_time():
    return "<p>16:05</p>"