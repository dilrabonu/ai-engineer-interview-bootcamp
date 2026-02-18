models = ["XGBoost", "LightGBM", "CatBoost"]
for i, model in enumerate(models):
    print(f"Model {i+1}: {model}")

children = ["Baxti", "Hasan", "Elbek", "Doniyor"]
for i, boy in enumerate(children):
    print(f"Child {i+1}: {boy}")

# zip
names = ["accuracy", "precision", "recall"]
scores = [0.9, 0.85, 0.87]
for name, value in zip(names, scores):
    print(f"{name}: {value:.2%}")

# dict
params = {"lr": 0.01, "epochs": 10, "dropout": 0.5}
for k, v in params.items():
    print(f"{k}: {v}")

# Match case
word = "Family"
match word:
    case "Father":
        print("Male")
    case "Family":
        print("Success")
    case _:
        print("Unknown")

point = (0, 5)
match point:
    case (0, y):
        print("Y-axis")

# *args
def compute_mean(*values):
    return sum(values) / len(values)

print(compute_mean(1, 2, 3, 4, 5))
# *kwargs
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_info(name="John", age=30, city="New York")

# Lambda
models = [
    {"name": "XGBoost", "accuracy": 0.9},
    {"name": "LightGBM", "accuracy": 0.85},
    {"name": "CatBoost", "accuracy": 0.87}
]
sorted_models = sorted(models, key=lambda m: m["accuracy"], reverse=True)
print(sorted_models)

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))


# Genartor lazy, remeber steps and continue and save memory
def generator_batch(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

# Iterator
nums = [1, 2, 3, 4, 5, 6]
it = iter(nums)
print(next(it))
print(next(it))