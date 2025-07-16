import pandas as pd
import matplotlib.pyplot as plt

# Load wallet scores
df = pd.read_csv("/mnt/data/wallet_scores.csv")

# Create bins for score ranges: 0–100, 101–200, ..., 901–1000
bins = list(range(0, 1100, 100))
labels = [f"{i}-{i+99}" for i in bins[:-1]]

# Assign score bins
df['score_range'] = pd.cut(df['score'], bins=bins, labels=labels, right=False)

# Count wallets in each score range
score_distribution = df['score_range'].value_counts().sort_index()

# Plot histogram
plt.figure(figsize=(10, 6))
score_distribution.plot(kind='bar', color='#3498db', edgecolor='black')
plt.title("Wallet Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save plot
output_path = "/mnt/data/score_distribution.png"
plt.savefig(output_path)
output_path
