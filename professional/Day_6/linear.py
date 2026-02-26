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