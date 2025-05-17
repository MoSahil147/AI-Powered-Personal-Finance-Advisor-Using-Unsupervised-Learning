# backend/tips_engine.py

from model.predict_cluster import predict_user_cluster

# Rule-based saving/investment suggestions mapped by cluster
cluster_tips = {
    0: [
        "You're spending a high amount on discretionary items. Try cutting down shopping by 15% to save more.",
        "Consider reducing OTT subscriptions. Canceling one could save ₹500/month.",
        "You’re in the low-saver cluster. Set automated savings of ₹200/week."
    ],
    1: [
        "Your spending pattern is balanced. Try investing your savings in a low-risk SIP.",
        "Shift part of your fixed expenses like travel to more economical options (e.g., monthly metro pass).",
        "Increase your saving rate by just 5% and grow your yearly savings significantly."
    ],
    2: [
        "Great job! You’re a high-saver. Consider investing in index funds or mutual funds.",
        "Explore high-yield savings accounts to get better returns.",
        "Maintain this discipline and consider diversifying investments in equity or gold."
    ]
}

def get_saving_tips(user_input_dict):
    """
    Accepts user input dictionary with 10 financial features.
    Returns tips based on predicted cluster.
    """
    cluster = predict_user_cluster(user_input_dict)
    return {
        "cluster": int(cluster),
        "tips": cluster_tips[cluster]
    }