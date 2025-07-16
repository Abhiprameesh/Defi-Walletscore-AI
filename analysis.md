# 📊 Wallet Score Analysis (analysis.md)

This document summarizes the outcome of applying the DeFi-Walletscore-AI pipeline to 100,000 Aave V2 protocol transactions. Our goal was to assign credit scores (0–1000) to wallets, with higher scores indicating safer, more reliable DeFi users.

---

## 📥 Task Recap (as per instruction)

Your task was to:

- Develop a machine learning model that scores wallets based on their historical transaction behavior.
- Implement a one-step script that takes a raw JSON file as input and outputs a CSV of wallet scores.
- Create this file, `analysis.md`, to analyze and explain the behavior of wallets based on score ranges.

---

## 📊 Score Distribution (Grouped by 100s)

| Score Range | Wallet Count | Approx. % |
|-------------|--------------|-----------|
| 0–100       | 124          | 3.57%     |
| 101–200     | 218          | 6.27%     |
| 201–300     | 388          | 11.18%    |
| 301–400     | 472          | 13.60%    |
| 401–500     | 536          | 15.45%    |
| 501–600     | 601          | 17.31%    |
| 601–700     | 459          | 13.23%    |
| 701–800     | 312          | 8.99%     |
| 801–900     | 201          | 5.79%     |
| 901–1000    | 158          | 4.55%     |

📌 Total Wallets Scored: 3469

## Score Distribution Histogram
![alt text](<score_distribution.png>)

---

## ⚠️ Behavior of Wallets in Lower Score Ranges (0–300)

Wallets that scored below 300 displayed one or more of the following traits:

- One-off transactions, often limited to a single borrow or liquidation.
- Zero or minimal repayment behavior.
- High volatility in asset usage or abnormal transaction bursts.
- Frequent liquidations (via liquidationCall events).
- Short lifespan — usually interacting in less than 2 or 3 timestamps.
- Potential bot-like or flashloan-driven behavior.

🟥 These wallets are considered high-risk and potentially harmful for protocol stability.

---

## ✅ Behavior of Wallets in Higher Score Ranges (800–1000)

Wallets that scored above 800 showed consistent, trustworthy patterns:

- Engaged in multiple deposit → borrow → repay cycles.
- Maintained a healthy borrow-to-repay ratio over time.
- No recorded liquidation calls.
- Spread interactions over multiple block timestamps.
- Handled diverse tokens and used pools responsibly.

🟩 These users represent ideal lending partners: responsible, consistent, and long-term engaged.

---

## 📌 Summary Table

| Score Band   | Risk Interpretation         | Dominant Behavior                           |
|--------------|-----------------------------|----------------------------------------------|
| 0–300        | High risk / exploitative    | Flash loans, single borrows, liquidations   |
| 301–600      | Moderate activity           | Limited repayments, small asset usage       |
| 601–800      | Balanced behavior           | Good repayment record, some red flags       |
| 801–1000     | Highly reliable             | Long-term usage, no liquidation, consistent |

---

## 📎 Notes

- The model uses engineered features such as transaction type frequencies, ratios, diversity scores, and wallet lifespan.
- Scores were normalized to fall within [0, 1000] using MinMax scaling.
- Histograms and insights were derived after generating wallet_scores.csv

---

## 📂 Output Files

- wallet_scores.csv — Wallet addresses and final scores.
- score_distribution.png — Visual plot of score distribution.
- analysis.md — This file.


