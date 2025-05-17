# backend/model/predict_cluster.py

import numpy as np
import joblib

# Load the trained scaler and model
scaler = joblib.load('backend/model/scaler.pkl')
kmeans = joblib.load('backend/model/kmeans_model.pkl')

# Function to predict user cluster based on input features
def predict_user_cluster(user_input_dict):
    """
    user_input_dict should be a dictionary with the following keys:
    'saving_rate', 'food_pct', 'travel_pct', 'shopping_pct',
    'bills_pct', 'subscriptions_pct', 'others_pct',
    'recurring_expense_ratio', 'discretionary_expense_ratio',
    'essential_expense_ratio'
    """
    feature_order = [
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

    input_vector = np.array([user_input_dict[feature] for feature in feature_order]).reshape(1, -1)
    input_scaled = scaler.transform(input_vector)
    cluster = kmeans.predict(input_scaled)[0]
    return cluster