"""
Utility functions for Bitcoin sentiment analysis
===============================================

Common helper functions and utilities used across the project.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings

def suppress_warnings():
    """Suppress common warnings for cleaner output."""
    warnings.filterwarnings('ignore')

def format_currency(amount):
    """Format amount as currency string."""
    return f"${amount:,.2f}"

def format_percentage(value):
    """Format value as percentage string."""
    return f"{value:.1f}%"

def calculate_win_rate(pnl_series):
    """Calculate win rate from PnL series."""
    if len(pnl_series) == 0:
        return 0.0
    return (pnl_series > 0).sum() / len(pnl_series) * 100

def get_sentiment_color(sentiment):
    """Get color for sentiment visualization."""
    color_map = {
        'Extreme Fear': 'darkred',
        'Fear': 'red', 
        'Neutral': 'gray',
        'Greed': 'green',
        'Extreme Greed': 'darkgreen'
    }
    return color_map.get(sentiment, 'gray')

def validate_required_columns(df, required_columns, data_type="data"):
    """Validate that dataframe has required columns."""
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns in {data_type}: {missing_columns}")
    return True

def safe_numeric_conversion(series, column_name):
    """Safely convert series to numeric, handling errors."""
    try:
        return pd.to_numeric(series, errors='coerce')
    except Exception as e:
        print(f"Warning: Could not convert {column_name} to numeric: {e}")
        return series

def print_section_header(title):
    """Print formatted section header."""
    print("\n" + "="*50)
    print(title.upper())
    print("="*50)

def print_subsection_header(title):
    """Print formatted subsection header."""
    print(f"\n{title}:")

def create_output_directory(path):
    """Create output directory if it doesn't exist."""
    import os
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created output directory: {path}")

def get_date_range_string(start_date, end_date):
    """Get formatted date range string."""
    return f"{start_date} to {end_date}"

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe ratio for returns series."""
    if len(returns) == 0 or returns.std() == 0:
        return 0.0
    
    excess_returns = returns.mean() - risk_free_rate/252  # Daily risk-free rate
    return excess_returns / returns.std() * np.sqrt(252)  # Annualized

def get_performance_summary(pnl_series):
    """Get comprehensive performance summary."""
    if len(pnl_series) == 0:
        return {
            'total_trades': 0,
            'total_pnl': 0,
            'avg_pnl': 0,
            'win_rate': 0,
            'max_win': 0,
            'max_loss': 0,
            'profit_factor': 0
        }
    
    winning_trades = pnl_series[pnl_series > 0]
    losing_trades = pnl_series[pnl_series < 0]
    
    total_wins = winning_trades.sum() if len(winning_trades) > 0 else 0
    total_losses = abs(losing_trades.sum()) if len(losing_trades) > 0 else 0
    
    return {
        'total_trades': len(pnl_series),
        'total_pnl': pnl_series.sum(),
        'avg_pnl': pnl_series.mean(),
        'win_rate': calculate_win_rate(pnl_series),
        'max_win': pnl_series.max(),
        'max_loss': pnl_series.min(),
        'profit_factor': total_wins / total_losses if total_losses > 0 else float('inf')
    }