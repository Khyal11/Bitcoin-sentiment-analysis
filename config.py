"""
Configuration file for Bitcoin Sentiment Analysis
================================================

Contains configuration parameters and settings for the analysis.
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / 'data'
OUTPUT_DIR = PROJECT_ROOT / 'outputs'
SRC_DIR = PROJECT_ROOT / 'src'

# Data file paths
HISTORICAL_DATA_PATH = DATA_DIR / 'historical_data.csv'
SENTIMENT_DATA_PATH = DATA_DIR / 'fear_greed_index.csv'

# Analysis parameters
ANALYSIS_CONFIG = {
    'min_trades_per_sentiment': 1,  # Minimum trades required for sentiment analysis
    'risk_free_rate': 0.02,  # Annual risk-free rate for Sharpe ratio calculation
    'confidence_level': 0.95,  # Confidence level for statistical tests
}

# Visualization settings
VISUALIZATION_CONFIG = {
    'figure_size': (15, 12),
    'dpi': 300,
    'style': 'default',
    'color_palette': 'husl',
    'save_format': 'png',
}

# Sentiment color mapping
SENTIMENT_COLORS = {
    'Extreme Fear': 'darkred',
    'Fear': 'red',
    'Neutral': 'gray', 
    'Greed': 'green',
    'Extreme Greed': 'darkgreen'
}

# Required columns for data validation
REQUIRED_HISTORICAL_COLUMNS = [
    'Account', 'Coin', 'Execution Price', 'Size USD', 'Side'
]

REQUIRED_SENTIMENT_COLUMNS = [
    'value', 'classification'
]

# Output file names
OUTPUT_FILES = {
    'comprehensive_analysis': 'sentiment_analysis_comprehensive.png',
    'basic_analysis': 'sentiment_analysis_basic.png',
    'time_series_analysis': 'time_series_analysis.png',
    'report': 'analysis_report.txt'
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': OUTPUT_DIR / 'analysis.log'
}

def ensure_directories():
    """Ensure all required directories exist."""
    directories = [DATA_DIR, OUTPUT_DIR]
    for directory in directories:
        directory.mkdir(exist_ok=True)

def get_config():
    """Get complete configuration dictionary."""
    return {
        'paths': {
            'project_root': PROJECT_ROOT,
            'data_dir': DATA_DIR,
            'output_dir': OUTPUT_DIR,
            'src_dir': SRC_DIR,
            'historical_data': HISTORICAL_DATA_PATH,
            'sentiment_data': SENTIMENT_DATA_PATH,
        },
        'analysis': ANALYSIS_CONFIG,
        'visualization': VISUALIZATION_CONFIG,
        'sentiment_colors': SENTIMENT_COLORS,
        'required_columns': {
            'historical': REQUIRED_HISTORICAL_COLUMNS,
            'sentiment': REQUIRED_SENTIMENT_COLUMNS,
        },
        'output_files': OUTPUT_FILES,
        'logging': LOGGING_CONFIG,
    }