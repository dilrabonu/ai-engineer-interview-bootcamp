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

# ==============================
# STEP 1 PARSE LOGS
# ==============================
parsed = []
for line in training_logs:
    parts = line.split()
    data = {}

    for item in parts:
        k, v = item.split("=", 1)
        if k == "epoch":
            data[k] = int(v)
        else:
            data[k] = float(v)
    parsed.append(data)
print("All parsed data:", parsed)
# ==============================
# STEP 2 FIND LOWEST LOSS
# ==============================
best_row = min(parsed, key=lambda d: d["loss"])
best_epoch = best_row["epoch"]
print("Best epoch (lowest loss):", best_epoch)

# ===============================
# STEP 3 CALCULATE IMPROVEMENT
# ===============================
acc_ep1 = parsed[0]["accuracy"]
acc_ep5 = parsed[-1]["accuracy"]
improvement = acc_ep5 - acc_ep1
print("Accuracy improvement:", improvement, f"({improvement*100:.0f}%)")


# ===============================
# STEP 4 RETURN EPOCHS
# ===============================
high_acc_epochs = [d["epoch"] for d in parsed if d["accuracy"] > 0.75]
print("High accuracy epochs:", high_acc_epochs)