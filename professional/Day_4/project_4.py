"""
Task:
Implement Linear/Logistic Regression from scratch No sklearn
se NumPy to implement gradient descent, loss calculation, and weight updates
"""
# Linear Regression from scratch
"""
Pseudo-code:
intialize w = zeros(d), b=0
repeat for epochs:
    y_hat = Xw +b
    loss = mean((y_hat - y)^2)
    dw = (2/n) * X^T (y_hat - y)
    db = (2/n) * sum(y_hat - y)
    w = w -lr *db
"""
import numpy as np 

class LinearRegressionGD:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs 
        self.w = None
        self.b = None
        self.loss_history = []
    
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).reshape(-1)
    
    
        n, d = X.shape

        self.w = np.zeros(d)
        self.b = 0.0

        for _ in range(self.epochs):
            y_hat = self.predict(X) #forward pass
            error = y_hat - y # residuals

            loss = np.mean(error ** 2) # MSE
            self.loss_history.append(loss)

            # Gradient vectorized
            dw = (2.0 / n) * (X.T @ error)
            db = (2.0 / n) * np.sum(error)

            # Gradient descent update
            self.w -= self.lr * dw
            self.b -= self.lr * db
        return self

    def predict(self, X):
        X = np.asarray(X, dtype=float)
        return X @ self.w _ self.b


