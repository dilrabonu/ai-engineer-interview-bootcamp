import torch 
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(10,1)

optimizer = optim.Adam(model.parameters(), lr=0.01)

scheduler = optim.lr_scheduler.StepLR(
    optimizer,
    step_size=10,
    gamma=0.1
)
loss_fn = nn.MSELoss()

for epoch in range(30):
    x = torch.randn(32,10)
    y = torch.randn(32,1)

    pred = model(x)

    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    scheduler.step()

    print("epoch:", epoch, "lr:", optimizer.param_groups[0]['lr'])