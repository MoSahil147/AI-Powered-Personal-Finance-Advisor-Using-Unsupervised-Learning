# backend/model/train_model.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

# Load the synthetic dataset
df = pd.read_csv("backend/model/synthetic_personal_finance_data.csv")

# Select features for training
features = [
    'saving_rate',
    'food_pct',
    'travel_pct',
    'shopping_pct',
    'bills_pct',
    'subscriptions_pct',
    'others_pct',
    'recurring_expense_ratio',
    'discretionary_expense_ratio',
    'essential_expense_ratio'
]

X = df[features]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the KMeans model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Save the scaler and model
joblib.dump(scaler, 'backend/model/scaler.pkl')
joblib.dump(kmeans, 'backend/model/kmeans_model.pkl')

print("KMeans model and scaler saved to backend/model/")