import joblib
import pandas as pd
import numpy as np

model = joblib.load('model.pkl')

def predict(df: pd.DataFrame):
    return int(np.exp(model.predict(df))[0])