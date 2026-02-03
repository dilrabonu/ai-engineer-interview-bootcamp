
import numpy as np

class SimpleNeuralNetwork:
    def __init__(self, layer_sizes, learning_rate=0.01):
        """
        Initialize the neural network with given layer sizes and learning rate.
        
        Args:
            layer_sizes: List of integers representing the number of neurons in each layer
            learning_rate: Learning rate for gradient descent
        """
        self.layers = layer_sizes
        self.lr = learning_rate
        self.params = self._init_params()

    def _init_params(self):
        """
        Initialize network parameters (weights and biases) for all layers.
        """
        params = {}

        for i in range(1, len(self.layers)):
            params[f'W{i}'] = np.random.randn(self.layers[i], self.layers[i-1]) * np.sqrt(2.0 / self.layers[i-1])
            params[f'b{i}'] = np.zeros((self.layers[i], 1))
        return params

    def _relu(self, Z):
        """RELU: max(0, Z)"""
        return np.maximum(0, Z)

    def _relu_derivative(self, Z):
        """RELU derivative: 1 if Z > 0, 0 otherwise"""
        return (Z > 0).astype(float)

    def _sigmoid(self, Z):
        """Sigmoid 1/(1+e^-z)"""
        return 1 / (1 + np.exp(-np.clip(Z, -500, 500)))

    def _sigmoid_derivative(self, Z):
        """ Sigmoid derivative: 0(1-0)"""
        return A * (1 - A)

    def forward(self, X):
        """
        Forward propagation through the network.
        
        Args:
            X: Input data
            
        Returns:
            Output of the network
        """
        cache = {'A0': X}
        A = X
        
        for i in range(1, len(self.layers)):
            Z = self.params[f'W{i}'] @ A + self.params[f'b{i}']

            # apply activation
            if i == len(self.layers) - 1:
                A = self._sigmoid(Z)
            else:
                A = self._relu(Z)

            cache[f'Z{i}'] = Z
            cache[f'A{i}'] = A

        return A, cache

    def compute_loss(self, Y_pred, Y_true):
        """Binary cross entropy loss"""
        m = Y_true.shape[1]
        Y_pred = np.clip(Y_pred, 1e-10, 1 - 1e-10)
        loss = -1/m * np.sum(Y_true * np.log(Y_pred) + (1 - Y_true) *np.log(1 - Y_pred))
        return loss

    def backward(self, Y, cache):
        """
        Backward propagation through the network.
        
        Args:
            Y: True labels
            cache: Cache from forward propagation
            
        Returns:
            Gradients for all parameters
        """
        m = Y.shape[1]
        grads = {}
        L = len(self.layers) - 1

        dA = -(Y / cache[f'A{L}'] - (1 - Y) / (1 - cache[f'A{L}']))

        for i in reversed(range(1, len(self.layers))):
            if i == L:
                dZ = dA * self._sigmoid_derivative(cache[f'A{i}'])
            else:
                dZ = dA * self._relu_derivative(cache[f'Z{i}'])

            grads[f'dW{i}'] = 1/m * dZ @ cache[f'A{i-1}'].T
            grads[f'db{i}'] = 1/m * np.sum(dZ, axis=1, keepdims=True)

            if i > 1:
                dA = self.params[f'W{i}'].T @ dZ
        return grads

    def update(self, grads):
        """Gradient descent update"""
        for i in range(1, len(self.layers)):
            self.params[f'W{i}'] -= self.lr * grads[f'dW{i}']
            self.params[f'b{i}'] -= self.lr * grads[f'db{i}']

    def train(self, X, Y, epochs=1000, verbose=False):
        """
        Train the neural network.
        
        Args:
            X: Training data
            Y: Training labels
            epochs: Number of training iterations
            verbose: Whether to print the cost every 100 iterations
        """
        for epoch in range(epochs):
            Y_pred, cache = self.forward(X)

            loss = self.compute_loss(Y_pred, Y)

            grads = self.backward(Y, cache)

            self.update(grads)

            if verbose and epoch % 100 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}")

        return loss
    def predict(self, X, threshold=0.5):
        """Make predictions"""
        probs, _ = self.forward(X)
        return (probs > threshold).astype(int), probs
        
if __name__ == "__main__":
    # Create XOR dataset
    np.random.seed(42)
    X = np.random.randn(2, 1000)
    Y = ((X[0, :] > 0) ^ (X[1, :] > 0)).astype(int).reshape(1, -1)
    
    # Create and train network
    nn = SimpleNeuralNetwork([2, 4, 4, 1], learning_rate=0.1)
    nn.train(X, Y, epochs=1000, verbose=True)
    
    # Test
    test_X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]]).T
    preds, probs = nn.predict(test_X)
    
    print("\nXOR Test:")
    for i in range(4):
        print(f"{test_X[:, i]} → {preds[0, i]} (prob: {probs[0, i]:.3f})")


