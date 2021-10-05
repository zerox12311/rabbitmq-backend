from flask import Flask, abort
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route('/api/mock1/<id>')
def mock1(id):
    if random.randint(0, 10) > 3:
        abort(400)
    else:
        return f'api_mock1 {id}'


@app.route('/api/mock2/<content>')
def mock2(content):
    return f'Success mock2, got {content}'