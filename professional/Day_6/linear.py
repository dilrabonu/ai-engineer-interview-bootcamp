class LinearRegressionCF:
    def fit(self, X, y):
        n = X.shape[0]
        X, b = np.column.stack([np.ones(n), X]) # add bias column
        self.theta = np.linalg.inv(X.b.T @ X.b) @ X.b.T @ y 
        self.bias = self.theta[0]
        self.weights = self.theta[1:]
        return self
    def predict(self, X):
        return X @ self.weights + self.bias

# Gradient descent
class LinearRegressionGD:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0

        for epoch in range(self.epochs):
            y_pred = X @ self.w + self.b 
            error = y_pred - y