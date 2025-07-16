import json
import pandas as pd
from features import extract_features
from score import compute_credit_score

# Step 1: Load JSON data
with open("user_transactions.json", "r") as f:
    transactions = json.load(f)

print("✅ JSON loaded. Total transactions:", len(transactions))

# Step 2: Group transactions by wallet
wallet_dict = {}

for tx in transactions:
    wallet = tx.get("userWallet")  # ✅ FIXED FIELD
    if wallet:
        wallet_dict.setdefault(wallet, []).append(tx)

print("✅ Grouped transactions by wallet. Total unique wallets:", len(wallet_dict))

# Step 3: Compute scores
wallet_scores = []

for wallet_address, tx_list in wallet_dict.items():
    features = extract_features(tx_list)
    score = compute_credit_score(features)
    wallet_scores.append({
        "wallet": wallet_address,
        "score": score
    })

# Step 4: Save to CSV
df_scores = pd.DataFrame(wallet_scores)
df_scores.to_csv("wallet_scores.csv", index=False)
print("✅ All scores saved to wallet_scores.csv")
