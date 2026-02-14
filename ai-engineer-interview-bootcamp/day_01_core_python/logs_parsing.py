training_logs = [
    "epoch=1 loss=0.8 accuracy=0.65",
    "epoch=2 loss=0.6 accuracy=0.72",
    "epoch=3 loss=0.5 accuracy=0.78",
    "epoch=4 loss=0.45 accuracy=0.81",
    "epoch=5 loss=0.4 accuracy=0.83"
]

# Your tasks:
# 1. Parse each log into a dictionary with keys: epoch, loss, accuracy
# 2. Find the epoch with the lowest loss
# 3. Calculate the improvement in accuracy from epoch 1 to epoch 5
# 4. Return all epochs where accuracy > 0.75

# BRR
#================================
# STEP 1 Parsed
#================================

parsed = []
for log in training_logs:
    parts = log.split()
    data = {}

    for part in parts:
        k, v = part.split("=", 1)
        if k == "epoch":
            data[k] = int(v)
        else:
            data[k] = float(v)
    parsed.append(data)

print("All parsed data:", parsed)

#=============================
# STEP 2 Find best epoch
#=============================

lowest_loss = float("inf")
best_epoch = None

for d in parsed:
    if d["loss"] < lowest_loss:
        lowest_loss = d["loss"]
        best_epoch = d["epoch"]
print("Best epoch in (Lowest loss):", best_epoch)

#================================
# STEP 3 Calculate improvements
#================================

first_acc = parsed[0]["accuracy"]
last_acc = parsed[-1]["accuracy"]

improvement = last_acc - first_acc
print(f"Accuracy improvement: {improvement:.2f}")

#======================================
# STEP 4 Find epochs with high accuracy
#======================================

high_acc_epoch = []

for d in parsed:
    if d["accuracy"] > 0.75:
        high_acc_epoch.append(d["epoch"])
print("High accuracy epochs:", high_acc_epoch)