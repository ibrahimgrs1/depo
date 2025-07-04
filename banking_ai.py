import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("banking.csv")

df.columns = df.columns.str.strip()

x = df["English Q/A (Part 1)"]
y = df["English Q/A (Part 2)"]

cv = CountVectorizer()
x = cv.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=22)
model = RandomForestClassifier()
model.fit(x_train, y_train)


input = input("Please enter your message: ")
vektor = cv.transform([input])
print("Predict:", model.predict(vektor)[0])