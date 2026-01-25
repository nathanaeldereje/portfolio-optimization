# src/eda.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

def plot_closing_prices(df: pd.DataFrame, title="Historical Closing Prices"):
    """Plots the closing prices of the assets."""
    plt.figure(figsize=(14, 7))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)
    
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_daily_returns(df: pd.DataFrame):
    """Plots daily returns to visualize volatility."""
    plt.figure(figsize=(14, 7))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column, alpha=0.7)
    
    plt.title("Daily Returns (Volatility)")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rolling_stats(df: pd.DataFrame, window=30):
    """Plots rolling mean and standard deviation."""
    plt.figure(figsize=(14, 7))
    for column in df.columns:
        rolling_mean = df[column].rolling(window=window).mean()
        rolling_std = df[column].rolling(window=window).std()
        plt.plot(df.index, rolling_std, label=f'{column} {window}-Day Rolling Std')
        
    plt.title(f"Rolling Volatility ({window} Days)")
    plt.xlabel("Date")
    plt.ylabel("Volatility (Std Dev)")
    plt.legend()
    plt.grid(True)
    plt.show()

def check_stationarity(series, name="Series"):
    """
    Performs Augmented Dickey-Fuller test to check for stationarity.
    """
    print(f"\n--- Augmented Dickey-Fuller Test: {name} ---")
    result = adfuller(series.dropna())
    labels = ['ADF Statistic', 'p-value', '#Lags Used', 'Number of Observations Used']
    
    for value, label in zip(result, labels):
        print(f"{label} : {value}")
        
    if result[1] <= 0.05:
        print("Result: Strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is STATIONARY.")
    else:
        print("Result: Weak evidence against null hypothesis, time series has a unit root, indicating it is NON-STATIONARY.")

def decompose_series(series, model='additive', period=252):
    """
    Decomposes the time series into Trend, Seasonality, and Residuals.
    """
    result = seasonal_decompose(series, model=model, period=period)
    fig = result.plot()
    fig.set_size_inches(14, 10)
    plt.show()
    
def calculate_risk_metrics(returns_df: pd.DataFrame):
    """
    Calculates VaR (95%) and Sharpe Ratio.
    """
    metrics = pd.DataFrame(index=returns_df.columns)
    
    # Value at Risk (95% confidence)
    # Using historical method: the 5th percentile of returns
    metrics['VaR_95'] = returns_df.quantile(0.05)
    
    # Sharpe Ratio (assuming 0 risk-free rate for simplicity, or 2% annualized)
    risk_free_rate = 0.02 / 252 # Daily approximation
    mean_return = returns_df.mean()
    std_dev = returns_df.std()
    
    metrics['Sharpe_Ratio'] = (mean_return - risk_free_rate) / std_dev
    
    # Annualized Sharpe
    metrics['Annualized_Sharpe'] = metrics['Sharpe_Ratio'] * np.sqrt(252)
    
    return metrics