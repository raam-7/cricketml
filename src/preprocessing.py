import pandas as pd

def prepare_features(df):

    df["strike_rate"] = (df["runs"] / df["balls"]) * 100

    features = df[["runs", "balls", "strike_rate"]]

    target = df["final_runs"]

    return features, target