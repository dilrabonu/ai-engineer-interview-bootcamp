import numpy as np

original = np.arange(12).reshape(3, 4)
print(original)
view = original[1:]
copy = original[1:].copy()
print(view)
print(copy)
# SVD & PCA from Scratch
U, S, Vt = np.linalg.svd(X, full_matrices=False)

k = 2
X_approx = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
# PCA from scratch using SVD:
class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components

    def fit(self, X):
        self.mean = X.mean(axis=0)
        X_centered = X - self_mean
        U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
        self.components = Vt[:self.n_components]
        total_var = np.sum(S**2) / (len(X) - 1)
        self.explained_variance_ratio = S[:self.n_components]**2 / total_var
            (S[:self.n_components]** 2 / (len(X) -1)) / total_var
        return self

    def transform(self, X):
        return (X - self.mean) @ self.components.T

# GroupBy
df.groupby('education').agg(
    avg_income=('income', 'mean'),
    count=('target', 'count'),
    target_rate=('target', 'mean'),
)
# Multiple groupby
df.groupby(['education', 'city'])['income'].agg(['mean', 'std', 'count'])
df['income_zscore'] = df.groupby('education')['income'].transform(
    lambda x: (x - x.mean()) / x.std()
)
df.groupby('education').apply(
    lambda g: g.nlargest(3, 'income')
)
# Merge, Concat, Pivot
pd.merge(users, orders, on='user_id', how='inner')
pd.merge(users, orders, on='user_id', how='left')
pd.merge(users, orders, on='user_id', how='outer')

pd.concat([df1, df2], axis=0, ignore_index=True)
pd.concat([df1, df2], axis=1)

df.pivot_table(values='income', index='education',
    columns='target', aggfunc='mean')
pd.melt(wide_df, id_vars='model', var_name='metric', value_name='score')