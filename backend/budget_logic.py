# backend/budget_logic.py

def prepare_user_features(income, expenses_dict):
    """
    Prepares the 10 financial features required for model prediction.
    
    Parameters:
    - income (float): User's income amount (daily, weekly, or monthly)
    - expenses_dict (dict): Category-wise user expenses, must include:
        'Food', 'Travel', 'Shopping', 'Bills', 'Subscriptions', 'Others'
    
    Returns:
    - dict: Feature dictionary to pass into prediction/tip engine
    """
    total_expense = sum(expenses_dict.values())
    saving_amount = income - total_expense
    saving_rate = round((saving_amount / income) * 100, 2)

    recurring = expenses_dict.get('Subscriptions', 0) + expenses_dict.get('Bills', 0)
    discretionary = expenses_dict.get('Shopping', 0) + expenses_dict.get('Others', 0)
    essential = expenses_dict.get('Food', 0) + expenses_dict.get('Travel', 0)

    return {
        'saving_rate': saving_rate,
        'food_pct': round((expenses_dict['Food'] / income) * 100, 2),
        'travel_pct': round((expenses_dict['Travel'] / income) * 100, 2),
        'shopping_pct': round((expenses_dict['Shopping'] / income) * 100, 2),
        'bills_pct': round((expenses_dict['Bills'] / income) * 100, 2),
        'subscriptions_pct': round((expenses_dict['Subscriptions'] / income) * 100, 2),
        'others_pct': round((expenses_dict['Others'] / income) * 100, 2),
        'recurring_expense_ratio': round((recurring / income) * 100, 2),
        'discretionary_expense_ratio': round((discretionary / income) * 100, 2),
        'essential_expense_ratio': round((essential / income) * 100, 2)
    }