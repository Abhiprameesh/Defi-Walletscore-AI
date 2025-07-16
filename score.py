def compute_credit_score(features):
    score = 500  

    score += features["deposit_sum"] * 0.05
    score += features["repay_sum"] * 0.1
    score -= features["borrow_sum"] * 0.07
    score -= features["liquidation_count"] * 50

    return int(min(1000, max(0, score)))  # clip b/w 0 and 1000
