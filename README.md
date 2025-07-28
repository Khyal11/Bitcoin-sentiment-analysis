# 📊 Bitcoin Sentiment vs Trader Performance Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)

Analyze how market sentiment (Fear/Greed Index) influences real trading performance using Hyperliquid historical data.

---

## 🧠 Key Objectives

* Correlate sentiment with trading performance (PnL, volume, win rate)
* Identify behavioral patterns under different market moods
* Generate visual insights and strategy takeaways

---

## ⚙️ Features

* Clean & preprocess both datasets
* Merge sentiment and trading timelines
* Analyze PnL, trade size, and behavior across sentiment types
* Generate charts & insights automatically

---

## 🗂️ Structure

```
Bitcoin-sentiment-analysis/
├── src/                  # Code modules
├── data/                 # Input datasets
├── outputs/              # Generated visualizations
├── main.py               # Run analysis
├── requirements.txt
└── README.md
```

---

## 📥 Setup

```bash
git clone https://github.com/Khyal11/Bitcoin-sentiment-analysis
cd Bitcoin-sentiment-analysis
pip install -r requirements.txt
python main.py
```

Ensure both datasets are in the `data/` folder:

* `historical_data.csv`
* `fear_greed_index.csv`

---

## 📊 Output Highlights

* PnL by market sentiment
* Win rates across fear/greed phases
* Trading volume distribution
* Visual dashboards saved in `outputs/`

Example screenshots attached in examples/.
---
