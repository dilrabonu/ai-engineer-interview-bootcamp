# list for DL dynamic data
training_losses = [] # will grow during the training
for epoch in range(1000):
    loss = train_one_epoch()
    training_losses.append(loss)

# Tuple for fixed data
MODEL_CONFIG = {
    "architecture": (784, 256, 128, 10), # layers sizes shouldn't change
    "input_shape": (28,28, 1), # image dimension - fixed
    "split_ratio": (0.8, 0.1, 0.1) #train/val/test - constant    
}

# Tuples as a dictionary for caching
prediction_cache = {}

def cashed_predict(model, features_tuple):
    if features_tuple not in prediction_cashe:
        prediction_cashe[features_tuple] = model.predict(features_tuple)
    return prediction_cashe[features_tuple]


# list 
training_losses = []
for epoch in range(1000):
    loss = train_one_epoch()
    training_losses.append(loss)

# Tuple
MODEL_CONFIG = {
    "architecture": (784, 256, 128, 10), # layers sizes should not chan ge
    "input_shape": (28, 28, 1), # image dimension fixed
    "ratio_split": (0.8, 0.1, 0.1) # train/val/test - constant
}

# as a dictionary
predict_cashe = {}
def cashed_predict(model, feauters_tuple):
    if feautures_tuple not in predict_cashe:
        predict_cashe[feautures_tuple] = model.predict(features_tuple)
    return predict_cashe[feautures_tuple]

my_cashe = {}


def cashed_predict(model, input_data):
    input_cashe = tuple(input_data.faltten()) # array
    # input_cashe = tuple(input_data) - list
    if input_cashe not in my_cashe:
        my_cashe[input_cashe] = model.predict(input_cashe)
    return my_cashe[input_cashe]

# data generator efficient for memory with yield especially for huge millions of images
def load_data_generator(n=1000000):
    """Generates data on-demand"""
    for i in range(n):
        yield i * 2 # Yields one value then pauses

# with list
def load_data_list(n=1000000):
    data = []
    for i in range(n):
        data.append(i * 2)
    return data

# ML process with generator
def batch_generator(X, y, batch_size=32):
    n_samples = len(X)
    
    for start_idx in range(0, n_samples, batch_size):
        end_idx = min(start_idx + batch_size, n_samples)

        yield X[start_idx:end_idx], y[start_idx:end_idx]

for epoch in range(10):
    for X_batch, y_batch in batch_generator(X_train, y_train, batch_size=64):
        pass 


# Task Coding
training_logs = [
    "epoch=1 loss=0.8 accuracy=0.65",
    "epoch=2 loss=0.6 accuracy=0.72",
    "epoch=3 loss=0.5 accuracy=0.78",
    "epoch=4 loss=0.45 accuracy=0.81",
    "epoch=5 loss=0.4 accuracy=0.83"
]

# Tasks:
# 1. Parse each log into a dictionary
# 2. Find the epoch with lowest loss
# 3. Calculate accuracy improvement from epoch 1 to 5
# 4. Return all epochs where accuracy > 0.75

# Step 1 Parse each log into a dictionary

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

# step 2
lowest_loss = float("inf")
best_epoch = None
for log in parsed:
    if log["loss"] < lowest_loss:
        lowest_loss = log["loss"]
        best_epoch = log["epoch"]

print("Best epoch (lowest losses):", best_epoch)

# step 3
first_acc = parsed[0]["accuracy"]
last_acc = parsed[-1]["accuracy"]

improvement = last_acc - first_acc
print(f"Accuracy improvement: {improvement:.2f}")

# Step 4
high_acc = []
for s in parsed:
    if s["accuracy"] > 0.75:
        high_acc.append(s["epoch"])
print("High accuracy:", high_acc)

# find dublicates
logs = [
    {"user_id": 123, "action": "login", "timestamp": "10:00"},
    {"user_id": 456, "action": "purchase", "timestamp": "10:05"},
    {"user_id": 123, "action": "view", "timestamp": "10:10"},  # duplicate
    {"user_id": 789, "action": "login", "timestamp": "10:15"},
    {"user_id": 456, "action": "logout", "timestamp": "10:20"},  # duplicate
    {"user_id": 123, "action": "logout", "timestamp": "10:25"},  # duplicate
]

# Return: [123, 456] (users who appear more than once)
unique = list(set([log["user_id"] for log in logs]))
print("Unique users:", unique)