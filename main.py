"""runs flask api and serves webpages"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """serves the api json"""
    return jsonify({'name': 'alice', 'email': 'alice@outlook.com'})


if __name__ == '__main__':
    app.run()
