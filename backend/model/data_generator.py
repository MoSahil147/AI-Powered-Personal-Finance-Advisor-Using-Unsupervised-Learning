# backend/model/data_generator.py

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

NUM_RECORDS = 1000
categories = ['Food', 'Travel', 'Shopping', 'Bills', 'Subscriptions', 'Others']
cycles = ['daily', 'weekly', 'monthly']
income_types = ['salary', 'pocket_money']

data = []

def generate_random_date():
    end_date = datetime.today()
    start_date = end_date - timedelta(days=180)
    return start_date + timedelta(days=random.randint(0, 180))

for i in range(NUM_RECORDS):
    user_id = random.randint(1000, 9999)
    cycle = random.choice(cycles)
    income_type = random.choice(income_types)
    date = generate_random_date().strftime("%Y-%m-%d")

    if cycle == 'daily':
        income = random.randint(200, 800)
    elif cycle == 'weekly':
        income = random.randint(1000, 5000)
    else:
        income = random.randint(4000, 30000)

    spend_ratios = np.random.dirichlet(np.random.uniform(0.5, 2.0, len(categories)), size=1)[0]
    spends = [round(income * r, 2) for r in spend_ratios]

    expense_dict = dict(zip(categories, spends))
    total_expense = sum(spends)
    saving_amount = round(income - total_expense, 2)
    saving_rate = round((saving_amount / income) * 100, 2)

    max_expense = max(spends)
    num_expenses = random.randint(3, 12)

    recurring = expense_dict['Subscriptions'] + expense_dict['Bills']
    discretionary = expense_dict['Shopping'] + expense_dict['Others']
    essential = expense_dict['Food'] + expense_dict['Travel']

    data.append({
        'user_id': user_id,
        'date': date,
        'income_amount': income,
        'income_type': income_type,
        'budget_cycle': cycle,
        'total_expense': round(total_expense, 2),
        'saving_amount': saving_amount,
        'saving_rate': saving_rate,
        'food_pct': round((expense_dict['Food'] / income) * 100, 2),
        'travel_pct': round((expense_dict['Travel'] / income) * 100, 2),
        'shopping_pct': round((expense_dict['Shopping'] / income) * 100, 2),
        'bills_pct': round((expense_dict['Bills'] / income) * 100, 2),
        'subscriptions_pct': round((expense_dict['Subscriptions'] / income) * 100, 2),
        'others_pct': round((expense_dict['Others'] / income) * 100, 2),
        'max_single_expense': max_expense,
        'num_expense_entries': num_expenses,
        'recurring_expense_ratio': round((recurring / income) * 100, 2),
        'discretionary_expense_ratio': round((discretionary / income) * 100, 2),
        'essential_expense_ratio': round((essential / income) * 100, 2)
    })

df = pd.DataFrame(data)
df.to_csv("backend/model/synthetic_personal_finance_data.csv", index=False)
print("Synthetic dataset saved to backend/model/synthetic_personal_finance_data.csv")