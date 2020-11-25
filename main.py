"""runs flask api and serves web pages"""
import database
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """renders front page"""
    return render_template('index.html')


@app.route('/send_results', methods=['POST'])
def send_results():
    """sends the api json results"""
    # if request.method == 'POST':
    #     search_term = request.form['search_term']
    #     results = {'name': 'alice', 'email': 'alice@outlook.com'}
    #     # run fx here to get results, needs to return dictionary
    #     # return jsonify(results.get(search_term))
    #     return recommender.df.get(0)
    return None


if __name__ == '__main__':
    app.run()
    # dash_app.main()

