"""
Data Loading and Cleaning Module
===============================

Handles loading, cleaning, and preprocessing of historical trading data
and sentiment data for analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from .utils import validate_required_columns, safe_numeric_conversion, print_section_header

class DataLoader:
    """
    Handles loading and cleaning of trading and sentiment data.
    """
    
    def __init__(self):
        """Initialize the data loader."""
        self.historical_data = None
        self.sentiment_data = None
        self.merged_data = None
    
    def load_historical_data(self, file_path):
        """
        Load historical trading data from CSV file.
        
        Args:
            file_path (str): Path to historical data CSV file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            print(f"Loading historical trader data from {file_path}...")
            self.historical_data = pd.read_csv(file_path)
            print(f"Historical data loaded: {len(self.historical_data)} records")
            return True
            
        except FileNotFoundError:
            print(f"Error: Historical data file not found at {file_path}")
            return False
        except Exception as e:
            print(f"Error loading historical data: {e}")
            return False
    
    def load_sentiment_data(self, file_path):
        """
        Load sentiment data from CSV file.
        
        Args:
            file_path (str): Path to sentiment data CSV file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            print(f"Loading sentiment data from {file_path}...")
            self.sentiment_data = pd.read_csv(file_path)
            print(f"Sentiment data loaded: {len(self.sentiment_data)} records")
            return True
            
        except FileNotFoundError:
            print(f"Error: Sentiment data file not found at {file_path}")
            return False
        except Exception as e:
            print(f"Error loading sentiment data: {e}")
            return False
    
    def clean_historical_data(self):
        """
        Clean and preprocess historical trading data.
        
        Returns:
            pd.DataFrame: Cleaned historical data or None if error
        """
        if self.historical_data is None:
            print("Error: Historical data not loaded")
            return None
        
        print("Cleaning historical trading data...")
        df = self.historical_data.copy()
        
        # Validate required columns
        required_columns = ['Account', 'Coin', 'Execution Price', 'Size USD', 'Side']
        try:
            validate_required_columns(df, required_columns, "historical data")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        
        # Handle timestamp columns
        df = self._process_timestamps(df)
        if df is None:
            return None
        
        # Extract date for merging
        df['date'] = df['datetime'].dt.date
        
        # Clean numeric columns
        numeric_columns = ['Execution Price', 'Size Tokens', 'Size USD', 'Closed PnL']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = safe_numeric_conversion(df[col], col)
        
        # Remove rows with invalid dates or critical missing data
        initial_count = len(df)
        df = df.dropna(subset=['datetime', 'date', 'Account', 'Coin', 'Execution Price', 'Size USD'])
        final_count = len(df)
        
        if initial_count != final_count:
            print(f"Removed {initial_count - final_count} rows with missing critical data")
        
        self.historical_data = df
        print("Historical data cleaning completed")
        return df
    
    def clean_sentiment_data(self):
        """
        Clean and preprocess sentiment data.
        
        Returns:
            pd.DataFrame: Cleaned sentiment data or None if error
        """
        if self.sentiment_data is None:
            print("Error: Sentiment data not loaded")
            return None
        
        print("Cleaning sentiment data...")
        df = self.sentiment_data.copy()
        
        # Validate required columns
        required_columns = ['value', 'classification']
        try:
            validate_required_columns(df, required_columns, "sentiment data")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        
        # Handle timestamp or date column
        df = self._process_sentiment_dates(df)
        if df is None:
            return None
        
        # Ensure value is numeric
        df['value'] = safe_numeric_conversion(df['value'], 'value')
        
        # Remove rows with invalid dates or missing data
        initial_count = len(df)
        df = df.dropna(subset=['date', 'value', 'classification'])
        final_count = len(df)
        
        if initial_count != final_count:
            print(f"Removed {initial_count - final_count} rows with missing data")
        
        self.sentiment_data = df
        print("Sentiment data cleaning completed")
        return df
    
    def merge_datasets(self):
        """
        Merge historical and sentiment data on date.
        
        Returns:
            pd.DataFrame: Merged dataset or None if error
        """
        if self.historical_data is None or self.sentiment_data is None:
            print("Error: Both datasets must be loaded and cleaned before merging")
            return None
        
        print("Merging datasets...")
        
        # Merge on date
        merged = pd.merge(
            self.historical_data,
            self.sentiment_data,
            on='date',
            how='inner'
        )
        
        print(f"Merged dataset created: {len(merged)} records")
        
        if len(merged) == 0:
            print("Warning: No matching dates found between datasets")
            return None
        
        self.merged_data = merged
        return merged
    
    def _process_timestamps(self, df):
        """Process timestamp columns in historical data."""
        if 'Timestamp IST' in df.columns:
            try:
                df['datetime'] = pd.to_datetime(df['Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce')
            except:
                print("Error: Could not parse 'Timestamp IST' column")
                return None
                
        elif 'Timestamp' in df.columns:
            try:
                # Try Unix timestamp in milliseconds first
                df['datetime'] = pd.to_datetime(df['Timestamp'], unit='ms', errors='coerce')
                
                # If that fails, try seconds
                if df['datetime'].isna().all():
                    df['datetime'] = pd.to_datetime(df['Timestamp'], unit='s', errors='coerce')
                    
            except:
                print("Error: Could not parse 'Timestamp' column")
                return None
        else:
            print("Error: No valid timestamp column found in historical data")
            return None
        
        # Check if datetime parsing was successful
        if df['datetime'].isna().all():
            print("Error: All timestamp values could not be parsed")
            return None
            
        return df
    
    def _process_sentiment_dates(self, df):
        """Process date/timestamp columns in sentiment data."""
        if 'timestamp' in df.columns:
            try:
                # Convert Unix timestamp to datetime
                df['date'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce').dt.date
            except:
                print("Error: Could not parse 'timestamp' column in sentiment data")
                return None
                
        elif 'date' in df.columns:
            try:
                # Try multiple date formats
                df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
                if df['date'].isna().all():
                    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
                if df['date'].isna().all():
                    df['date'] = pd.to_datetime(df['date'], errors='coerce')
                    
                df['date'] = df['date'].dt.date
            except:
                print("Error: Could not parse 'date' column in sentiment data")
                return None
        else:
            print("Error: No valid timestamp or date column found in sentiment data")
            return None
        
        # Check if date parsing was successful
        if pd.Series(df['date']).isna().all():
            print("Error: All date values could not be parsed")
            return None
            
        return df
    
    def get_data_summary(self):
        """
        Get summary of loaded and processed data.
        
        Returns:
            dict: Summary statistics
        """
        summary = {
            'historical_loaded': self.historical_data is not None,
            'sentiment_loaded': self.sentiment_data is not None,
            'merged_available': self.merged_data is not None
        }
        
        if self.historical_data is not None:
            summary['historical_records'] = len(self.historical_data)
            summary['historical_date_range'] = (
                self.historical_data['date'].min(),
                self.historical_data['date'].max()
            )
        
        if self.sentiment_data is not None:
            summary['sentiment_records'] = len(self.sentiment_data)
            summary['sentiment_date_range'] = (
                self.sentiment_data['date'].min(),
                self.sentiment_data['date'].max()
            )
        
        if self.merged_data is not None:
            summary['merged_records'] = len(self.merged_data)
            summary['merged_date_range'] = (
                self.merged_data['date'].min(),
                self.merged_data['date'].max()
            )
        
        return summary