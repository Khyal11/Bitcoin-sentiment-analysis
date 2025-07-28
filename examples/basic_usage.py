"""
Basic Usage Examples for Bitcoin Sentiment Analysis
==================================================

This file demonstrates various ways to use the Bitcoin sentiment analysis toolkit.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path to import modules
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from src.analyzer import BitcoinSentimentAnalyzer
from src.data_loader import DataLoader
from src.visualizer import SentimentVisualizer

def example_1_basic_analysis():
    """
    Example 1: Basic complete analysis
    """
    print("=" * 60)
    print("EXAMPLE 1: Basic Complete Analysis")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = BitcoinSentimentAnalyzer()
    
    # Run complete analysis
    success = analyzer.run_complete_analysis(
        historical_path='data/historical_data.csv',
        sentiment_path='data/fear_greed_index.csv',
        visualization_type='comprehensive'
    )
    
    return success

def example_2_step_by_step_analysis():
    """
    Example 2: Step-by-step analysis with custom parameters
    """
    print("=" * 60)
    print("EXAMPLE 2: Step-by-Step Analysis")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = BitcoinSentimentAnalyzer(output_dir='examples/outputs')
    
    # Step 1: Load data
    print("Step 1: Loading data...")
    if not analyzer.load_data('data/historical_data.csv', 'data/fear_greed_index.csv'):
        print("Failed to load data")
        return False
    
    # Step 2: Clean and prepare data
    print("Step 2: Cleaning and preparing data...")
    if not analyzer.clean_and_prepare_data():
        print("Failed to clean data")
        return False
    
    # Step 3: Explore data
    print("Step 3: Exploring data...")
    analyzer.explore_data()
    
    # Step 4: Analyze sentiment-performance relationship
    print("Step 4: Analyzing sentiment-performance relationship...")
    sentiment_analysis, win_rates = analyzer.analyze_sentiment_performance_relationship()
    
    # Step 5: Create visualizations
    print("Step 5: Creating visualizations...")
    analyzer.create_visualizations('all')
    
    # Step 6: Generate insights
    print("Step 6: Generating insights and strategies...")
    insights = analyzer.generate_insights_and_strategies()
    
    return True

def example_3_data_loader_only():
    """
    Example 3: Using only the data loader component
    """
    print("=" * 60)
    print("EXAMPLE 3: Data Loader Only")
    print("=" * 60)
    
    # Initialize data loader
    loader = DataLoader()
    
    # Load data
    loader.load_historical_data('data/historical_data.csv')
    loader.load_sentiment_data('data/fear_greed_index.csv')
    
    # Clean data
    historical_clean = loader.clean_historical_data()
    sentiment_clean = loader.clean_sentiment_data()
    
    # Merge data
    merged = loader.merge_datasets()
    
    # Get summary
    summary = loader.get_data_summary()
    print("Data Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    return merged is not None

def example_4_visualizer_only():
    """
    Example 4: Using only the visualizer component
    """
    print("=" * 60)
    print("EXAMPLE 4: Visualizer Only")
    print("=" * 60)
    
    # First, get some data
    loader = DataLoader()
    loader.load_historical_data('data/historical_data.csv')
    loader.load_sentiment_data('data/fear_greed_index.csv')
    loader.clean_historical_data()
    loader.clean_sentiment_data()
    merged_data = loader.merge_datasets()
    
    if merged_data is None:
        print("No data available for visualization")
        return False
    
    # Initialize visualizer
    visualizer = SentimentVisualizer(output_dir='examples/outputs')
    
    # Create different types of visualizations
    print("Creating comprehensive analysis...")
    visualizer.create_comprehensive_analysis(merged_data, 'example_comprehensive')
    
    print("Creating basic analysis...")
    visualizer.create_basic_analysis(merged_data, 'example_basic')
    
    print("Creating time series analysis...")
    visualizer.create_time_series_analysis(merged_data, 'example_time_series')
    
    return True

def example_5_custom_analysis():
    """
    Example 5: Custom analysis with specific focus
    """
    print("=" * 60)
    print("EXAMPLE 5: Custom Analysis - Focus on Fear Periods")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = BitcoinSentimentAnalyzer()
    
    # Load and prepare data
    analyzer.load_data('data/historical_data.csv', 'data/fear_greed_index.csv')
    analyzer.clean_and_prepare_data()
    
    # Focus on Fear periods only
    fear_data = analyzer.merged_data[
        analyzer.merged_data['classification'].str.contains('Fear', na=False)
    ]
    
    print(f"Total records: {len(analyzer.merged_data)}")
    print(f"Fear-related records: {len(fear_data)}")
    
    if len(fear_data) > 0:
        # Analyze fear periods specifically
        print("\nFear Period Analysis:")
        fear_analysis = fear_data.groupby('classification').agg({
            'Closed PnL': ['count', 'sum', 'mean'],
            'Size USD': ['sum', 'mean']
        }).round(2)
        print(fear_analysis)
        
        # Create visualization for fear periods only
        analyzer.visualizer.create_comprehensive_analysis(
            fear_data, 'fear_periods_analysis'
        )
    
    return True

def run_all_examples():
    """
    Run all examples
    """
    print("Running all examples...")
    
    # Create examples output directory
    os.makedirs('examples/outputs', exist_ok=True)
    
    examples = [
        ("Basic Analysis", example_1_basic_analysis),
        ("Step-by-Step Analysis", example_2_step_by_step_analysis),
        ("Data Loader Only", example_3_data_loader_only),
        ("Visualizer Only", example_4_visualizer_only),
        ("Custom Analysis", example_5_custom_analysis),
    ]
    
    results = {}
    
    for name, example_func in examples:
        print(f"\n{'='*80}")
        print(f"Running: {name}")
        print(f"{'='*80}")
        
        try:
            success = example_func()
            results[name] = "✅ Success" if success else "❌ Failed"
        except Exception as e:
            results[name] = f"❌ Error: {str(e)}"
            print(f"Error in {name}: {e}")
    
    # Print summary
    print(f"\n{'='*80}")
    print("EXAMPLES SUMMARY")
    print(f"{'='*80}")
    
    for name, result in results.items():
        print(f"{name}: {result}")
    
    print(f"{'='*80}")

if __name__ == "__main__":
    # Check if specific example is requested
    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        
        examples_map = {
            '1': example_1_basic_analysis,
            '2': example_2_step_by_step_analysis,
            '3': example_3_data_loader_only,
            '4': example_4_visualizer_only,
            '5': example_5_custom_analysis,
        }
        
        if example_num in examples_map:
            print(f"Running Example {example_num}...")
            success = examples_map[example_num]()
            sys.exit(0 if success else 1)
        else:
            print(f"Invalid example number: {example_num}")
            print("Available examples: 1, 2, 3, 4, 5")
            sys.exit(1)
    else:
        # Run all examples
        run_all_examples()