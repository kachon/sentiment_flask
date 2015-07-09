import os
from flask import Flask, jsonify
from sklearn.datasets import fetch_20newsgroups

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/test')
def test():
    categories = ['alt.atheism', 'soc.religion.christian',
                  'comp.graphics', 'sci.med']
    twenty_train = fetch_20newsgroups(subset='train',
                    categories=categories, shuffle=True, random_state=42)
    return jsonify(results=twenty_train.target_names)

@app.route('/channel/<id>')
def channel(id):
    return id

if __name__ == '__main__':
    app.run(debug=True)
