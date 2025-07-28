"""
Visualization Module
===================

Creates comprehensive visualizations for sentiment analysis results.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from .utils import get_sentiment_color, format_currency, format_percentage, create_output_directory

class SentimentVisualizer:
    """
    Creates visualizations for sentiment analysis results.
    """
    
    def __init__(self, output_dir='outputs'):
        """
        Initialize the visualizer.
        
        Args:
            output_dir (str): Directory to save output files
        """
        self.output_dir = output_dir
        create_output_directory(output_dir)
        
        # Set plotting style
        plt.style.use('default')
        sns.set_palette("husl")
    
    def create_comprehensive_analysis(self, merged_data, save_name='sentiment_analysis_comprehensive'):
        """
        Create comprehensive analysis visualizations.
        
        Args:
            merged_data (pd.DataFrame): Merged dataset
            save_name (str): Name for saved file
        """
        if merged_data is None or len(merged_data) == 0:
            print("Error: No data available for visualization")
            return
        
        print("Creating comprehensive visualizations...")
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Bitcoin Market Sentiment vs Trader Performance Analysis', 
                    fontsize=16, fontweight='bold', y=0.98)
        
        # 1. Total PnL by Sentiment
        self._plot_total_pnl_by_sentiment(merged_data, axes[0, 0])
        
        # 2. Average PnL by Sentiment  
        self._plot_average_pnl_by_sentiment(merged_data, axes[0, 1])
        
        # 3. Trade Count by Sentiment
        self._plot_trade_count_by_sentiment(merged_data, axes[0, 2])
        
        # 4. Trading Volume by Sentiment
        self._plot_volume_by_sentiment(merged_data, axes[1, 0])
        
        # 5. Win Rate by Sentiment
        self._plot_win_rate_by_sentiment(merged_data, axes[1, 1])
        
        # 6. PnL vs Fear/Greed Scatter
        self._plot_pnl_vs_sentiment_scatter(merged_data, axes[1, 2])
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Save the plot
        save_path = f"{self.output_dir}/{save_name}.png"
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Comprehensive analysis saved as '{save_path}'")
        
        return fig
    
    def create_basic_analysis(self, merged_data, save_name='sentiment_analysis_basic'):
        """
        Create basic analysis visualizations (original format).
        
        Args:
            merged_data (pd.DataFrame): Merged dataset
            save_name (str): Name for saved file
        """
        if merged_data is None or len(merged_data) == 0:
            print("Error: No data available for visualization")
            return
        
        print("Creating basic visualizations...")
        
        # Create figure with 2x2 subplots (original layout)
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Bitcoin Market Sentiment vs Trader Performance Analysis', 
                    fontsize=16, fontweight='bold', y=0.98)
        
        # 1. PnL Distribution by Sentiment
        ax1 = axes[0, 0]
        sentiment_pnl = merged_data.groupby('classification')['Closed PnL'].sum()
        if len(sentiment_pnl) > 0:
            colors = ['red' if 'Fear' in str(idx) else 'green' for idx in sentiment_pnl.index]
            sentiment_pnl.plot(kind='bar', ax=ax1, color=colors, alpha=0.7)
            ax1.set_title('Total PnL by Market Sentiment')
            ax1.set_ylabel('Total PnL ($)')
            ax1.tick_params(axis='x', rotation=45)
        else:
            ax1.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax1.transAxes)
        
        # 2. Trading Volume by Sentiment
        ax2 = axes[0, 1]
        sentiment_volume = merged_data.groupby('classification')['Size USD'].sum()
        if len(sentiment_volume) > 0:
            sentiment_volume.plot(kind='bar', ax=ax2, color='blue', alpha=0.7)
            ax2.set_title('Trading Volume by Market Sentiment')
            ax2.set_ylabel('Volume ($)')
            ax2.tick_params(axis='x', rotation=45)
        else:
            ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
        
        # 3. Fear/Greed Index Over Time
        ax3 = axes[1, 0]
        daily_sentiment = merged_data.groupby('date')['value'].mean()
        if len(daily_sentiment) > 0:
            ax3.plot(daily_sentiment.index, daily_sentiment.values, color='purple', linewidth=2)
            ax3.set_title('Fear/Greed Index Over Time')
            ax3.set_ylabel('Fear/Greed Index')
            ax3.tick_params(axis='x', rotation=45)
        else:
            ax3.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax3.transAxes)
        
        # 4. PnL vs Fear/Greed Index Scatter
        ax4 = axes[1, 1]
        if len(merged_data) > 0:
            scatter_colors = {'Fear': 'red', 'Extreme Fear': 'darkred', 'Greed': 'green', 'Extreme Greed': 'darkgreen'}
            for sentiment in merged_data['classification'].unique():
                data = merged_data[merged_data['classification'] == sentiment]
                ax4.scatter(data['value'], data['Closed PnL'], 
                           label=sentiment, alpha=0.6, 
                           color=scatter_colors.get(sentiment, 'gray'))
            
            ax4.set_title('PnL vs Fear/Greed Index')
            ax4.set_xlabel('Fear/Greed Index')
            ax4.set_ylabel('Closed PnL ($)')
            ax4.legend()
        else:
            ax4.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax4.transAxes)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Save the plot
        save_path = f"{self.output_dir}/{save_name}.png"
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Basic analysis saved as '{save_path}'")
        
        return fig
    
    def _plot_total_pnl_by_sentiment(self, data, ax):
        """Plot total PnL by sentiment."""
        sentiment_pnl = data.groupby('classification')['Closed PnL'].sum()
        if len(sentiment_pnl) > 0:
            colors = [get_sentiment_color(sentiment) for sentiment in sentiment_pnl.index]
            bars = sentiment_pnl.plot(kind='bar', ax=ax, color=colors, alpha=0.7)
            ax.set_title('Total PnL by Market Sentiment')
            ax.set_ylabel('Total PnL ($)')
            ax.tick_params(axis='x', rotation=45)
            
            # Add value labels on bars
            for i, v in enumerate(sentiment_pnl.values):
                ax.text(i, v + (max(sentiment_pnl.values) * 0.01), 
                       format_currency(v), ha='center', va='bottom')
        else:
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
    
    def _plot_average_pnl_by_sentiment(self, data, ax):
        """Plot average PnL by sentiment."""
        sentiment_avg_pnl = data.groupby('classification')['Closed PnL'].mean()
        if len(sentiment_avg_pnl) > 0:
            colors = [get_sentiment_color(sentiment) for sentiment in sentiment_avg_pnl.index]
            sentiment_avg_pnl.plot(kind='bar', ax=ax, color=colors, alpha=0.7)
            ax.set_title('Average PnL per Trade by Sentiment')
            ax.set_ylabel('Average PnL ($)')
            ax.tick_params(axis='x', rotation=45)
            
            # Add value labels
            for i, v in enumerate(sentiment_avg_pnl.values):
                ax.text(i, v + (max(sentiment_avg_pnl.values) * 0.01), 
                       format_currency(v), ha='center', va='bottom')
        else:
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
    
    def _plot_trade_count_by_sentiment(self, data, ax):
        """Plot trade count by sentiment."""
        trade_counts = data['classification'].value_counts()
        if len(trade_counts) > 0:
            colors = [get_sentiment_color(sentiment) for sentiment in trade_counts.index]
            trade_counts.plot(kind='bar', ax=ax, color=colors, alpha=0.7)
            ax.set_title('Number of Trades by Sentiment')
            ax.set_ylabel('Number of Trades')
            ax.tick_params(axis='x', rotation=45)
            
            # Add value labels
            for i, v in enumerate(trade_counts.values):
                ax.text(i, v + 0.1, f'{v}', ha='center', va='bottom')
        else:
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
    
    def _plot_volume_by_sentiment(self, data, ax):
        """Plot trading volume by sentiment."""
        sentiment_volume = data.groupby('classification')['Size USD'].sum()
        if len(sentiment_volume) > 0:
            sentiment_volume.plot(kind='bar', ax=ax, color='blue', alpha=0.7)
            ax.set_title('Total Trading Volume by Sentiment')
            ax.set_ylabel('Volume ($)')
            ax.tick_params(axis='x', rotation=45)
            
            # Add value labels
            for i, v in enumerate(sentiment_volume.values):
                ax.text(i, v + (max(sentiment_volume.values) * 0.01), 
                       format_currency(v), ha='center', va='bottom')
        else:
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
    
    def _plot_win_rate_by_sentiment(self, data, ax):
        """Plot win rate by sentiment."""
        win_rates = data.groupby('classification').apply(
            lambda x: (x['Closed PnL'] > 0).sum() / len(x) * 100
        )
        if len(win_rates) > 0:
            colors = [get_sentiment_color(sentiment) for sentiment in win_rates.index]
            win_rates.plot(kind='bar', ax=ax, color=colors, alpha=0.7)
            ax.set_title('Win Rate by Sentiment')
            ax.set_ylabel('Win Rate (%)')
            ax.tick_params(axis='x', rotation=45)
            
            # Add value labels
            for i, v in enumerate(win_rates.values):
                ax.text(i, v + 1, format_percentage(v), ha='center', va='bottom')
        else:
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
    
    def _plot_pnl_vs_sentiment_scatter(self, data, ax):
        """Plot PnL vs sentiment scatter plot."""
        if len(data) > 0:
            scatter_colors = {
                'Fear': 'red', 
                'Extreme Fear': 'darkred', 
                'Greed': 'green', 
                'Extreme Greed': 'darkgreen',
                'Neutral': 'gray'
            }
            
            for sentiment in data['classification'].unique():
                subset = data[data['classification'] == sentiment]
                ax.scatter(subset['value'], subset['Closed PnL'], 
                          label=sentiment, alpha=0.6, 
                          color=scatter_colors.get(sentiment, 'gray'))
            
            ax.set_title('PnL vs Fear/Greed Index')
            ax.set_xlabel('Fear/Greed Index')
            ax.set_ylabel('Closed PnL ($)')
            ax.legend()
        else:
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
    
    def create_time_series_analysis(self, merged_data, save_name='time_series_analysis'):
        """
        Create time series analysis visualizations.
        
        Args:
            merged_data (pd.DataFrame): Merged dataset
            save_name (str): Name for saved file
        """
        if merged_data is None or len(merged_data) == 0:
            print("Error: No data available for time series visualization")
            return
        
        print("Creating time series analysis...")
        
        fig, axes = plt.subplots(3, 1, figsize=(15, 12))
        fig.suptitle('Time Series Analysis', fontsize=16, fontweight='bold')
        
        # Daily aggregation
        daily_data = merged_data.groupby('date').agg({
            'Closed PnL': 'sum',
            'Size USD': 'sum',
            'value': 'mean',
            'classification': 'first'
        }).reset_index()
        
        # 1. Daily PnL
        axes[0].plot(daily_data['date'], daily_data['Closed PnL'], marker='o', linewidth=2)
        axes[0].set_title('Daily PnL Over Time')
        axes[0].set_ylabel('Daily PnL ($)')
        axes[0].grid(True, alpha=0.3)
        
        # 2. Daily Volume
        axes[1].bar(daily_data['date'], daily_data['Size USD'], alpha=0.7, color='blue')
        axes[1].set_title('Daily Trading Volume Over Time')
        axes[1].set_ylabel('Daily Volume ($)')
        axes[1].grid(True, alpha=0.3)
        
        # 3. Fear/Greed Index
        axes[2].plot(daily_data['date'], daily_data['value'], marker='s', 
                    linewidth=2, color='purple')
        axes[2].set_title('Fear/Greed Index Over Time')
        axes[2].set_ylabel('Fear/Greed Index')
        axes[2].set_xlabel('Date')
        axes[2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save the plot
        save_path = f"{self.output_dir}/{save_name}.png"
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Time series analysis saved as '{save_path}'")
        
        return fig