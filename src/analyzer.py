"""
Core Analysis Module
===================

Main analysis engine for Bitcoin sentiment and trader performance analysis.
"""

import pandas as pd
import numpy as np
from .data_loader import DataLoader
from .visualizer import SentimentVisualizer
from .utils import (
    print_section_header, print_subsection_header, format_currency, 
    format_percentage, calculate_win_rate, get_performance_summary,
    suppress_warnings
)

class BitcoinSentimentAnalyzer:
    """
    Main analyzer for Bitcoin market sentiment and trader performance data.
    """
    
    def __init__(self, output_dir='outputs'):
        """
        Initialize the analyzer.
        
        Args:
            output_dir (str): Directory for output files
        """
        suppress_warnings()
        
        self.data_loader = DataLoader()
        self.visualizer = SentimentVisualizer(output_dir)
        self.output_dir = output_dir
        
        # Data properties
        self.historical_data = None
        self.sentiment_data = None
        self.merged_data = None
    
    def load_data(self, historical_path='data/historical_data.csv', sentiment_path='data/fear_greed_index.csv'):
        """
        Load historical trader data and sentiment data.
        
        Args:
            historical_path (str): Path to historical trader data CSV
            sentiment_path (str): Path to fear/greed index CSV
            
        Returns:
            bool: True if successful, False otherwise
        """
        print_section_header("Loading Data")
        
        # Load historical data
        if not self.data_loader.load_historical_data(historical_path):
            return False
        
        # Load sentiment data
        if not self.data_loader.load_sentiment_data(sentiment_path):
            return False
        
        # Store references
        self.historical_data = self.data_loader.historical_data
        self.sentiment_data = self.data_loader.sentiment_data
        
        return True
    
    def clean_and_prepare_data(self):
        """
        Clean and prepare the data for analysis.
        
        Returns:
            bool: True if successful, False otherwise
        """
        print_section_header("Data Cleaning and Preparation")
        
        # Clean historical data
        if self.data_loader.clean_historical_data() is None:
            print("Error: Failed to clean historical data")
            return False
        
        # Clean sentiment data
        if self.data_loader.clean_sentiment_data() is None:
            print("Error: Failed to clean sentiment data")
            return False
        
        # Merge datasets
        merged = self.data_loader.merge_datasets()
        if merged is None or len(merged) == 0:
            print("Error: Failed to merge datasets or merged dataset is empty")
            return False
        
        # Store references
        self.historical_data = self.data_loader.historical_data
        self.sentiment_data = self.data_loader.sentiment_data
        self.merged_data = self.data_loader.merged_data
        
        print("Data cleaning and preparation completed successfully")
        return True
    
    def explore_data(self):
        """
        Perform exploratory data analysis.
        """
        if self.merged_data is None or len(self.merged_data) == 0:
            print("Error: No merged data available. Please run clean_and_prepare_data() first.")
            return
        
        print_section_header("Exploratory Data Analysis")
        
        # Basic statistics
        print_subsection_header("1. Dataset Overview")
        print(f"   - Total merged records: {len(self.merged_data)}")
        print(f"   - Date range: {self.merged_data['date'].min()} to {self.merged_data['date'].max()}")
        print(f"   - Unique accounts: {self.merged_data['Account'].nunique()}")
        print(f"   - Unique symbols: {self.merged_data['Coin'].nunique()}")
        
        # Sentiment distribution
        print_subsection_header("2. Sentiment Distribution")
        sentiment_counts = self.merged_data['classification'].value_counts()
        for sentiment, count in sentiment_counts.items():
            percentage = (count / len(self.merged_data)) * 100
            print(f"   - {sentiment}: {count} ({percentage:.1f}%)")
        
        # Trading statistics
        print_subsection_header("3. Trading Statistics")
        if 'Closed PnL' in self.merged_data.columns:
            total_pnl = self.merged_data['Closed PnL'].sum()
            avg_pnl = self.merged_data['Closed PnL'].mean()
            print(f"   - Total PnL: {format_currency(total_pnl)}")
            print(f"   - Average PnL per trade: {format_currency(avg_pnl)}")
            
        if 'Size USD' in self.merged_data.columns:
            total_volume = self.merged_data['Size USD'].sum()
            avg_volume = self.merged_data['Size USD'].mean()
            print(f"   - Total trading volume: {format_currency(total_volume)}")
            print(f"   - Average trade size: {format_currency(avg_volume)}")
    
    def analyze_sentiment_performance_relationship(self):
        """
        Analyze the relationship between market sentiment and trader performance.
        
        Returns:
            tuple: (sentiment_analysis, win_rates)
        """
        if self.merged_data is None or len(self.merged_data) == 0:
            print("Error: No merged data available.")
            return None, None
        
        print_section_header("Sentiment-Performance Relationship Analysis")
        
        # Group by sentiment classification
        sentiment_analysis = self.merged_data.groupby('classification').agg({
            'Closed PnL': ['count', 'sum', 'mean', 'std'],
            'Size USD': ['sum', 'mean'],
            'value': 'mean'
        }).round(2)
        
        print_subsection_header("1. Performance by Market Sentiment")
        print(sentiment_analysis)
        
        # Calculate win rates by sentiment
        print_subsection_header("2. Win Rates by Sentiment")
        win_rates = self.merged_data.groupby('classification').apply(
            lambda x: calculate_win_rate(x['Closed PnL'])
        ).round(2)
        
        for sentiment, rate in win_rates.items():
            print(f"   - {sentiment}: {format_percentage(rate)}")
        
        # Detailed performance metrics
        print_subsection_header("3. Detailed Performance Metrics")
        for sentiment in self.merged_data['classification'].unique():
            subset = self.merged_data[self.merged_data['classification'] == sentiment]
            performance = get_performance_summary(subset['Closed PnL'])
            
            print(f"\n   {sentiment}:")
            print(f"     - Total trades: {performance['total_trades']}")
            print(f"     - Total PnL: {format_currency(performance['total_pnl'])}")
            print(f"     - Average PnL: {format_currency(performance['avg_pnl'])}")
            print(f"     - Win rate: {format_percentage(performance['win_rate'])}")
            print(f"     - Best trade: {format_currency(performance['max_win'])}")
            print(f"     - Worst trade: {format_currency(performance['max_loss'])}")
            if performance['profit_factor'] != float('inf'):
                print(f"     - Profit factor: {performance['profit_factor']:.2f}")
        
        return sentiment_analysis, win_rates
    
    def create_visualizations(self, visualization_type='comprehensive'):
        """
        Create visualizations for the analysis.
        
        Args:
            visualization_type (str): Type of visualization ('comprehensive', 'basic', 'time_series', 'all')
        """
        if self.merged_data is None or len(self.merged_data) == 0:
            print("Error: No merged data available for visualization.")
            return
        
        print_section_header("Creating Visualizations")
        
        if visualization_type in ['comprehensive', 'all']:
            self.visualizer.create_comprehensive_analysis(self.merged_data)
        
        if visualization_type in ['basic', 'all']:
            self.visualizer.create_basic_analysis(self.merged_data)
        
        if visualization_type in ['time_series', 'all']:
            self.visualizer.create_time_series_analysis(self.merged_data)
        
        print("Visualization creation completed")
    
    def generate_insights_and_strategies(self):
        """
        Generate insights and trading strategy recommendations.
        
        Returns:
            dict: Insights and recommendations
        """
        if self.merged_data is None or len(self.merged_data) == 0:
            print("Error: No merged data available.")
            return None
        
        print_section_header("Insights and Trading Strategies")
        
        # Calculate key metrics by sentiment
        sentiment_metrics = self.merged_data.groupby('classification').agg({
            'Closed PnL': ['mean', 'sum', 'count', 'std'],
            'Size USD': ['sum', 'mean'],
            'value': 'mean'
        }).round(2)
        
        # Find best performing sentiment
        avg_pnl_by_sentiment = sentiment_metrics['Closed PnL']['mean']
        best_sentiment = avg_pnl_by_sentiment.idxmax()
        best_avg_pnl = avg_pnl_by_sentiment.max()
        
        # Find most active sentiment
        trade_counts = sentiment_metrics['Closed PnL']['count']
        most_active_sentiment = trade_counts.idxmax()
        most_active_count = trade_counts.max()
        
        # Find lowest risk sentiment (lowest std dev)
        risk_by_sentiment = sentiment_metrics['Closed PnL']['std']
        lowest_risk_sentiment = risk_by_sentiment.idxmin()
        lowest_risk_std = risk_by_sentiment.min()
        
        # Generate insights
        insights = {
            'best_performing_sentiment': (best_sentiment, best_avg_pnl),
            'most_active_sentiment': (most_active_sentiment, most_active_count),
            'lowest_risk_sentiment': (lowest_risk_sentiment, lowest_risk_std),
            'sentiment_metrics': sentiment_metrics
        }
        
        print_subsection_header("Key Insights")
        print(f"   1. BEST PERFORMING SENTIMENT: {best_sentiment} with average PnL of {format_currency(best_avg_pnl)}")
        print(f"   2. MOST ACTIVE TRADING: {most_active_sentiment} with {most_active_count} trades")
        print(f"   3. LOWEST RISK SENTIMENT: {lowest_risk_sentiment} with PnL std dev of {format_currency(lowest_risk_std)}")
        
        # Generate strategy recommendations
        print_subsection_header("Recommended Trading Strategies")
        strategies = self._generate_strategy_recommendations(insights)
        
        for i, strategy in enumerate(strategies, 1):
            print(f"   {i}. {strategy}")
        
        return insights
    
    def _generate_strategy_recommendations(self, insights):
        """
        Generate trading strategy recommendations based on insights.
        
        Args:
            insights (dict): Analysis insights
            
        Returns:
            list: List of strategy recommendations
        """
        strategies = []
        
        best_sentiment = insights['best_performing_sentiment'][0]
        most_active_sentiment = insights['most_active_sentiment'][0]
        
        # Base strategies
        strategies.extend([
            f"CONTRARIAN STRATEGY: Consider increasing position sizes during 'Extreme Fear' periods if historical data shows recovery patterns.",
            f"MOMENTUM STRATEGY: Reduce exposure during sustained fear periods to minimize downside risk.",
            f"RISK MANAGEMENT: Implement tighter stop-losses during high-volatility sentiment periods.",
            f"POSITION SIZING: Adjust position sizes based on current fear/greed index levels.",
            f"TIMING STRATEGY: Use sentiment extremes as potential entry/exit signals for swing trading."
        ])
        
        # Sentiment-specific strategies
        if 'Fear' in best_sentiment:
            strategies.append(f"FEAR OPPORTUNITY: Historical data shows {best_sentiment} periods offer good trading opportunities.")
        
        if 'Greed' in best_sentiment:
            strategies.append(f"GREED CAUTION: While {best_sentiment} shows good average returns, consider taking profits during extreme greed.")
        
        # Volume-based strategies
        if most_active_sentiment != best_sentiment:
            strategies.append(f"ACTIVITY vs PERFORMANCE: Most trading happens during {most_active_sentiment}, but best performance is during {best_sentiment}.")
        
        return strategies
    
    def run_complete_analysis(self, historical_path='data/historical_data.csv', 
                            sentiment_path='data/fear_greed_index.csv',
                            visualization_type='comprehensive'):
        """
        Run the complete analysis pipeline.
        
        Args:
            historical_path (str): Path to historical data
            sentiment_path (str): Path to sentiment data
            visualization_type (str): Type of visualizations to create
            
        Returns:
            bool: True if successful, False otherwise
        """
        print("Starting Bitcoin Sentiment and Trader Performance Analysis...")
        print("=" * 60)
        
        # Load data
        if not self.load_data(historical_path, sentiment_path):
            print("Failed to load data. Analysis aborted.")
            return False
        
        # Clean and prepare data
        if not self.clean_and_prepare_data():
            print("Failed to clean and prepare data. Analysis aborted.")
            return False
        
        # Perform analysis
        self.explore_data()
        self.analyze_sentiment_performance_relationship()
        self.create_visualizations(visualization_type)
        self.generate_insights_and_strategies()
        
        print("=" * 60)
        print("Analysis completed successfully!")
        print(f"Check '{self.output_dir}/' directory for visualizations.")
        
        return True