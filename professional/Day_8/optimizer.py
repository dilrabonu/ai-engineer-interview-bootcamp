import torch 
import torch.nn as nn
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20,1)
)

loss_fn = nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(100):
    x = torch.randn(32,10)
    y = torch.randn(32,1)

    pred = model(x)

    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(loss.item())