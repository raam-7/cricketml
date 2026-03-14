import pandas as pd
import joblib

from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split

from preprocessing import prepare_features

df = pd.read_csv("data/batsman_dataset.csv")

X, y = prepare_features(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

joblib.dump(ridge, "models/ridge_model.pkl")
joblib.dump(lasso, "models/lasso_model.pkl")

print("Models saved!")