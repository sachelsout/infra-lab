# imports
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# iris data
iris = load_iris()
X, y = iris.data, iris.target

# training logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# saving the trained model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)