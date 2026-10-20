import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = load_diabetes(as_frame=True)
df = data.frame
print(df.describe())          # analisis data
print(df.corr()["target"].sort_values())  # fitur paling berpengaruh

X_train, X_test, y_train, y_test = train_test_split(
    df.drop(columns="target"), df["target"], test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
print("R2 score:", r2_score(y_test, model.predict(X_test)))