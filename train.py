import pickle
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


# Extract Data
def extract_data():
    data = load_iris()
    return data

# Preparing features
def preparing_features(data):
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.DataFrame(data.target,columns=['target'])
    return X,y

# Train Model
def train_model(X,y):
    model = DecisionTreeClassifier(max_depth=2)
    model.fit(X,y)
    return model

    # Serialize object
def serialize_object(model):
    with open("trained_classifier.pkl", "wb") as file:
        pickle.dump(model,file)

# Run training pipeline
def run():
    data = extract_data()
    X, y = preparing_features(data)
    model = train_model(X, y)
    serialize_object(model=model)


if __name__ == "__main__":
    run()
