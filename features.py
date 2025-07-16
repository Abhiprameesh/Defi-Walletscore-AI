from utils import safe_float

def extract_features(transactions):
    deposit_sum = 0
    borrow_sum = 0
    repay_sum = 0
    liquidation_count = 0
    redeem_sum = 0

    for tx in transactions:
        action = tx.get("action", "").lower()
        amount_raw = tx.get("actionData", {}).get("amount", 0)
        amount = safe_float(amount_raw) / 1e6  # Adjust for USDC-style decimals (6)

        if action == "deposit":
            deposit_sum += amount
        elif action == "borrow":
            borrow_sum += amount
        elif action == "repay":
            repay_sum += amount
        elif action == "liquidationcall":
            liquidation_count += 1
        elif action == "redeemunderlying":
            redeem_sum += amount

    return {
        "deposit_sum": deposit_sum,
        "borrow_sum": borrow_sum,
        "repay_sum": repay_sum,
        "liquidation_count": liquidation_count,
        "redeem_sum": redeem_sum
    }
