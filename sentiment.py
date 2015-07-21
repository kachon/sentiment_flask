import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
import cPickle

class SentimentClf(object):
    def __init__(self):
      self.clf_from_file = cPickle.load( open( "clf_pipeline.dat", "rb" ) )

    def predict(self, doc):
      return self.clf_from_file.predict_proba([doc])[0]

