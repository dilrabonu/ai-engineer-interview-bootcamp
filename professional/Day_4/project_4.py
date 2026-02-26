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
        return X @ self.w + self.b


#Logistic Regression from scratch
"""
initialize w = zeros(d) , b = 0
repeat for epochs:
    z = Xw + b
    p = sigmoid(z)
    loss = -mean(y*log(p) + (1-y)*log(1-p))
    dw = (1/n) * X^T(p-y)
    db = (1/n) *sum(p-y)
    w = w - lr *dw
    b = b - lr * db
"""
import numpy as np 
class LogisticRegressionGD:
    def__init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = None
        self.loss_history = []

    def _sigmoid(self, z):
        # Clip for numerical stability (prevents overflow in exp)
        z = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z))

    def predict_proba(self, X):
        X = np.asarray(X, dtype=float)
        z = X @ self.w + self.b
        return self._sigmoid(z)

    def predict(self, X, threshold=0.5):
        proba = self.predict_proba(X)
        return (proba >= threshold).astype(int)

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).reshape(-1)

        n, d = X.shape
        #Initialize parameters


