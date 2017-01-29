from whereami.learn import learn
from whereami.predict import locations, predict
from time import sleep

def whereami_predict():
    return predict()

def whereami_learn(location):
    learn(location)
