# html files have to be located in ./templates

from flask import Flask, render_template
import os

app = Flask(__name__)

# root url passed two variables
@app.route('/')
def index():
    return "HELLO 🌍"


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8080)
    
    