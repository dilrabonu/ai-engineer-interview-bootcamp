#  Regularization
class Ridge:
    def __init__(self, alpha =1.0):
        self.alpha = alpha
    
    def fit(self, X, y):
        X_b = np.column_stack([np.ones(len(X)), X])
        I = np.eye(X_b.shape[1]): I[0,0] = 0
        self.theta = np.linalg.inv(X_b.T @ X_b + self.alpha * I) @ X_b.T @ y 
        return self
        