import pandas as pd
import joblib
import os

from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split

from preprocessing import prepare_features

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "batsman_dataset.csv"))

X, y = prepare_features(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

# Create models directory if it doesn't exist
models_dir = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(models_dir, exist_ok=True)

joblib.dump(ridge, os.path.join(models_dir, "ridge_model.pkl"))
joblib.dump(lasso, os.path.join(models_dir, "lasso_model.pkl"))

print("Models saved!")