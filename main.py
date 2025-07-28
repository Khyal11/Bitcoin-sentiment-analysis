#!/usr/bin/env python3
"""
Bitcoin Market Sentiment and Trader Performance Analysis - Main Script
======================================================================

This is the main execution script for the Bitcoin sentiment analysis project.
It uses a modular architecture with separate components for data loading,
analysis, and visualization.

Usage:
    python main_modular.py

Author: Assignment Solution
Date: December 2024
Version: 1.1.0
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from src.analyzer import BitcoinSentimentAnalyzer

def main():
    """
    Main execution function.
    """
    print("Bitcoin Market Sentiment and Trader Performance Analysis")
    print("=" * 60)
    print("Version: 1.1.0 (Modular)")
    print("Author: Assignment Solution")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = BitcoinSentimentAnalyzer(output_dir='outputs')
    
    # Define data paths
    historical_path = 'data/historical_data.csv'
    sentiment_path = 'data/fear_greed_index.csv'
    
    # Check if data files exist
    if not os.path.exists(historical_path):
        print(f"Error: Historical data file not found at {historical_path}")
        print("Please ensure the file exists in the data/ directory.")
        return False
    
    if not os.path.exists(sentiment_path):
        print(f"Error: Sentiment data file not found at {sentiment_path}")
        print("Please ensure the file exists in the data/ directory.")
        return False
    
    # Run complete analysis
    success = analyzer.run_complete_analysis(
        historical_path=historical_path,
        sentiment_path=sentiment_path,
        visualization_type='all'  # Create all types of visualizations
    )
    
    if success:
        print("\n" + "=" * 60)
        print("✅ Analysis completed successfully!")
        print("📊 Check the 'outputs/' directory for generated visualizations")
        print("📈 Review the console output for detailed insights")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ Analysis failed. Please check the error messages above.")
        print("=" * 60)
    
    return success

def run_custom_analysis():
    """
    Run custom analysis with specific parameters.
    """
    print("Running Custom Analysis...")
    
    # Initialize analyzer
    analyzer = BitcoinSentimentAnalyzer(output_dir='outputs')
    
    # Load data
    if not analyzer.load_data('data/historical_data.csv', 'data/fear_greed_index.csv'):
        return False
    
    # Clean and prepare data
    if not analyzer.clean_and_prepare_data():
        return False
    
    # Run specific analysis components
    print("\n🔍 Running Exploratory Data Analysis...")
    analyzer.explore_data()
    
    print("\n📊 Analyzing Sentiment-Performance Relationship...")
    sentiment_analysis, win_rates = analyzer.analyze_sentiment_performance_relationship()
    
    print("\n📈 Creating Comprehensive Visualizations...")
    analyzer.create_visualizations('comprehensive')
    
    print("\n💡 Generating Insights and Strategies...")
    insights = analyzer.generate_insights_and_strategies()
    
    return True

if __name__ == "__main__":
    # Check command line arguments for custom analysis
    if len(sys.argv) > 1 and sys.argv[1] == '--custom':
        success = run_custom_analysis()
    else:
        success = main()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)