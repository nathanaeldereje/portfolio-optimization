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
    Extracts the Adjusted Close price. 
    If 'Adj Close' is missing (common with auto_adjust=True), it uses 'Close'.
    """
    adj_close_df = pd.DataFrame()
    
    for ticker in tickers:
        # Get the data for the specific ticker
        ticker_data = df[ticker]
        
        # Check if 'Adj Close' exists, otherwise use 'Close'
        if 'Adj Close' in ticker_data.columns:
            adj_close_df[ticker] = ticker_data['Adj Close']
        elif 'Close' in ticker_data.columns:
            print(f"Note: 'Adj Close' not found for {ticker}. Using 'Close' (likely already adjusted).")
            adj_close_df[ticker] = ticker_data['Close']
        else:
            raise KeyError(f"Neither 'Adj Close' nor 'Close' found for {ticker}")
            
    return adj_close_df

def calculate_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates daily percentage change (volatility).
    """
    return df.pct_change().dropna()