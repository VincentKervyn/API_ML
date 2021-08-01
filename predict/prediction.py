import pandas as pd
import numpy as np

import joblib

# import pickle

model = joblib.load(open('\model.pkl', 'rb'))


def predict(dataset):
    prediction = model.predict(dataset)
    return prediction