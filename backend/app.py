# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from budget_logic import prepare_user_features
from tips_engine import get_saving_tips

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "SmartSave AI Backend is Running"

@app.route('/api/analyze', methods=['POST'])
def analyze_expenses():
    data = request.json

    try:
        income = float(data['income'])
        expenses = data['expenses']  # Expected: dict with keys: Food, Travel, Shopping, Bills, Subscriptions, Others

        # Prepare features
        user_features = prepare_user_features(income, expenses)

        # Get tips and cluster
        result = get_saving_tips(user_features)

        return jsonify({
            'status': 'success',
            'input': user_features,
            'cluster': result['cluster'],
            'tips': result['tips']
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)