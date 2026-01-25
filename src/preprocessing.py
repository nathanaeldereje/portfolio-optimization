# src/preprocessing.py
import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Checks for missing values and handles them.
    """
    print("Checking for missing values...")
    missing = df.isnull().sum().sum()
    if missing > 0:
        print(f"Found {missing} missing values. Forward filling...")
        df.ffill(inplace=True)
        df.bfill(inplace=True) # Handle initial NaNs
    else:
        print("No missing values found.")
    
    return df

def get_adj_close(df: pd.DataFrame, tickers: list) -> pd.DataFrame:
    """
    Extracts only the Adjusted Close columns for analysis.
    """
    # Create a new DataFrame for Adj Close
    adj_close_df = pd.DataFrame()
    for ticker in tickers:
        adj_close_df[ticker] = df[ticker]['Adj Close']
    return adj_close_df

def calculate_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates daily percentage change (volatility).
    """
    return df.pct_change().dropna()