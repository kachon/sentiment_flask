import os
from flask import Flask, jsonify
from sklearn.datasets import fetch_20newsgroups
from yt import *
from sentiment import *
from flask import request
from sentiment import SentimentClf
from yt import Yt
import cPickle
import gzip

yt_obj = Yt()
clf_1 = cPickle.load( gzip.open( "clf_pipeline.pklz", "rb" ) )
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
  return jsonify(results=Yt().get_channel(id))

@app.route('/predict')
def predict():
  query = request.args.get('query')
  print "query %s" % (query)
  if query:
    return jsonify(results=SentimentClf().predict(query).tolist())
  else:
    return jsonify(results=[])

@app.route('/predict_channel/<id>')
def predict_channel(id):
  proba = predict_channel_comments(id)
  return jsonify(results=proba)

def predict_channel_comments(channel_id):
  comments = yt_obj.get_channel_comments(channel_id)
  for comment in comments:
    proba = clf_1.predict_proba([comment["comment"]])
    comment["proba"] = proba[0].tolist()
  return comments

if __name__ == '__main__':
  app.run(debug=True)
