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