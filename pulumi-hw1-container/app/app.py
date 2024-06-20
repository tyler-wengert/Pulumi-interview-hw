from flask import Flask
import os

app = Flask(__name__)

#get that environment variable that I added
msg = os.getenv('MESSAGE')

@app.route("/")
def index():
    return { "message": f"{msg}" }
