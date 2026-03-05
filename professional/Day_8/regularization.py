import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(20,64),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(64,1)
)
loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=0.01)

model.train()
for epoch in range(100):
    x = torch.randn(32,20)
    y = torch.randn(32,1)

    pred = model(x)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")