# DeFi Walletscore AI

This project aims to assign a credit score between 0 and 1000 to wallets interacting with the Aave V2 protocol, based solely on historical transaction behavior.

## 📊 Objective
Using a dataset of 100K+ DeFi transactions (deposits, borrows, repayments, redemptions, liquidations), we build an ML pipeline that:
- Extracts meaningful behavioral features from wallets.
- Trains a model to assess creditworthiness.
- Outputs a CSV with wallet addresses and their assigned scores.

## 🧠 Approach
1. Parsed raw JSON transaction file (~87MB) and grouped data by wallet.
2. Engineered behavioral features such as:
   - Count and volume of deposits, borrows, repayments
   - Borrow-to-deposit ratio
   - Default risk proxies (e.g., liquidation frequency)
   - Interaction span and frequency
3. Trained an XGBoost-based scoring model mapping behavior to credit score scale (0–1000).
4. Exported results to `wallet_scores.csv`.

## 🛠️ Project Structure
```bash
.
├── main.py                  # Entry point script
├── features.py              # Feature engineering logic
├── score.py                 # ML model and scoring logic
├── utils.py                 # JSON loader and helper functions
├── requirements.txt         # Dependencies
├── user_transactions.json   # Raw transaction data (locally ignored)
├── wallet_scores.csv        # Final wallet scores output
├── README.md
└── analysis.md              # Post-scoring insights and plots
```

## 🔧 Setup & Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run pipeline and generate wallet_scores.csv
python main.py
```

## 📌 Notes
- The file `user_transactions.json` is ignored via `.gitignore` and must be downloaded manually from:
  - JSON (87MB): https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view?usp=sharing
  - ZIP (10MB): https://drive.google.com/file/d/14ceBCLQ-BTcydDrFJauVA_PKAZ7VtDor/view?usp=sharing

## ⚙️ Dependencies
- Python 3.8+
- pandas, numpy, scikit-learn, xgboost, matplotlib

## 📬 Contact
Made by [Abhipramesh](https://github.com/Abhipramesh) — feel free to reach out for suggestions or collaboration.

---

> See `analysis.md` for detailed score breakdowns and insights.
