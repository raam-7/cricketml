import joblib
import numpy as np

model = joblib.load("models/ridge_model.pkl")

def predict_score(runs, balls):

    strike_rate = (runs / balls) * 100

    features = np.array([[runs, balls, strike_rate]])

    prediction = model.predict(features)

    return prediction[0]