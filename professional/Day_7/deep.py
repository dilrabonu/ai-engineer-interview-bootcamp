# Perceptron
import numpy as np 
class Perceptron:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.epochs):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.w) + self.b 
                y_pred = 1 if linear_output >= 0 else 0
                update = self.lr * (y[i] - y_pred)
                self.w += update * X[i]
                self.b += update
    def predict(self, X):
        linear_output = np.dot(X, self.w) + self.b 
        return npwhere(linear_output >= 0, 1, 0)