"""
Bitcoin Market Sentiment and Trader Performance Analysis Package
================================================================

A comprehensive analysis tool for examining the relationship between 
Bitcoin market sentiment and trader performance.

Author: Assignment Solution
Date: December 2024
"""

__version__ = "1.1.0"
__author__ = "Assignment Solution"

from .analyzer import BitcoinSentimentAnalyzer
from .data_loader import DataLoader
from .visualizer import SentimentVisualizer
from .utils import *

__all__ = [
    'BitcoinSentimentAnalyzer',
    'DataLoader', 
    'SentimentVisualizer'
]