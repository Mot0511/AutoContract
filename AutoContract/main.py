from flask import *

app = Flask(__name__, static_folder="static")

@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/contract')
def contract():
    pass

app.run()