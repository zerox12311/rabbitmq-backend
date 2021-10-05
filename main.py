from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route('/api/mock1/<id>')
def mock1(id):
    return f'api_mock1 {id}'


@app.route('/api/mock2/<content>')
def mock2(content):
    return f'Success mock2, got {content}'