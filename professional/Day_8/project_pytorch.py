import numpy as np 
import torch 
import torch.nn as nn
import torch.optim as optim

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler

# Load dataset
iris = load_iris()

X = iris.data.astype(np.float32)
y = iris.target.astype(np.int64)

# Normalization
scaler = StandardScaler()
X = scaler.fit_transform(X).astype(np.float32)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Convert to tensors
X_train = torch.tensor(X_train)
y_train = torch.tensor(y_train)
X_test = torch.tensor(X_test)
y_test = torch.tensor(y_test)

class MLP(nn.Module):
    def __init__(self, in_features=4, hidden=32, out_features=3, dropout_p=0.2):
        super().__init__()
        self.fc1 = nn.Linear(in_features, hidden)
        self.bn1 = nn.BatchNorm1d(hidden) # Normalization
        self.drop = nn.Dropout(dropout_p) # Regularization
        self.fc2 = nn.Linear(hidden, out_features)

        # Weight Initialization
        nn.init.kaiming_normal_(self.fc1.weight) # init for ReLU
        nn.init.zeros_(self.fc1.bias)
        nn.init.xavier_normal_(self.fc2.weight) # Xavier works for final Linear layer
        nn.init.zeros_(self.fc2.bias)

    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)
        x = torch.relu(x) # act function for non-linearity
        x = self.drop(x) # prevent overfitting
        logits = self.fc2(x) # prediction score logits
        return logits 

model = MLP()

# Loss function
loss_fn = nn.CrossEntropyLoss()

# Optimizer
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)

# Learning Rate
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.5)

# Training
epochs = 20
for epoch in range(1, epochs + 1):
    model.train()

    logits = model(X_train) # forward pass -> prediction(logits)
    loss = loss_fn(logits, y_train)

    optimizer.zero_grad() # clear old gradients
    loss.backward() # Backpropagation -> compute gradients
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step() # opt. updates weights
    scheduler.step() # adjusts lr

    if epoch % 20 == 0:
        lr = optimizer.param_groups[0]['lr']
        print(f"Epoch {epoch:03d} | loss={loss.item():.4f} | lr={lr:.6f}")

# Evaluate
model.eval()
with torch.no_grad():
    test_logits = model(X_test)
    preds = torch.argmax(test_logits, dim=1)
    acc = (preds == y_test).float().mean().item()

print("Test accuracy:", acc)


