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
