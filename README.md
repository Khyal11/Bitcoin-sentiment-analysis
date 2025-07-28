# 📊 Bitcoin Market Sentiment and Trader Performance Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

A comprehensive analysis tool that examines the relationship between Bitcoin market sentiment (Fear/Greed Index) and trader performance data from Hyperliquid to uncover patterns and insights for smarter trading strategies.

## 📊 Project Overview

This project analyzes how market sentiment affects trading behavior and performance by:
- Correlating Fear/Greed Index data with actual trading results
- Identifying patterns in trading volume during different market sentiments
- Providing insights for better trading strategies
- Generating comprehensive visualizations and reports

## 🚀 Features

- **Data Loading & Cleaning**: Robust data processing for historical trading and sentiment data
- **Sentiment Analysis**: Correlation between market fear/greed and trading performance
- **Performance Metrics**: Win rates, PnL analysis, and volume patterns by sentiment
- **Visualizations**: Comprehensive charts showing sentiment-performance relationships
- **Strategy Insights**: Data-driven trading strategy recommendations

## 📁 Project Structure

```
BlockChainProject/
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Data loading and cleaning utilities
│   ├── analyzer.py             # Core analysis engine
│   ├── visualizer.py           # Visualization and plotting
│   └── utils.py                # Helper functions and utilities
├── data/
│   ├── historical_data.csv     # Trading data from Hyperliquid
│   └── fear_greed_index.csv    # Fear/Greed Index data
├── outputs/
│   └── (generated charts and reports)
├── main.py                     # Main execution script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🛠️ Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd BlockChainProject
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure data files are present**
   - Place `historical_data.csv` in the `data/` directory
   - Place `fear_greed_index.csv` in the `data/` directory

## 📊 Data Format

### Historical Trading Data (`historical_data.csv`)
Required columns:
- `Account`: Trader wallet address
- `Coin`: Trading symbol
- `Execution Price`: Trade execution price
- `Size USD`: Trade size in USD
- `Side`: BUY/SELL
- `Timestamp IST` or `Timestamp`: Trade timestamp
- `Closed PnL`: Profit/Loss for the trade

### Fear/Greed Index Data (`fear_greed_index.csv`)
Required columns:
- `timestamp` or `date`: Date of the sentiment reading
- `value`: Fear/Greed index value (0-100)
- `classification`: Sentiment classification (Fear, Extreme Fear, Greed, etc.)


### Command Line Usage
```bash
python main.py
```

## 📈 Analysis Results

The analysis provides:

1. **Exploratory Data Analysis**
   - Dataset overview and statistics
   - Sentiment distribution
   - Trading volume and PnL summaries

2. **Sentiment-Performance Relationship**
   - PnL performance by market sentiment
   - Win rates across different sentiment periods
   - Trading volume patterns

3. **Visualizations**
   - Total PnL by market sentiment
   - Trading volume distribution
   - Fear/Greed index trends over time
   - PnL vs sentiment scatter plots

4. **Strategic Insights**
   - Best performing sentiment periods
   - Risk-adjusted returns analysis
   - Trading strategy recommendations

