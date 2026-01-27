# src/backtester.py
import pandas as pd
import numpy as np

def calculate_portfolio_returns(returns_df, weights):
    """
    Calculates the daily returns of a portfolio given asset weights.
    """
    # Ensure weights are in the same order as columns
    portfolio_returns = (returns_df * pd.Series(weights)).sum(axis=1)
    return portfolio_returns

def calculate_cumulative_returns(returns):
    """Calculates cumulative growth of $1."""
    return (1 + returns).cumprod()

def calculate_drawdown(cumulative_returns):
    """Calculates the Peak-to-Trough decline."""
    rolling_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - rolling_max) / rolling_max
    return drawdown.min()

def get_backtest_metrics(returns, risk_free_rate=0.02):
    """
    Calculates Total Return, Annualized Return, Sharpe Ratio, and Max Drawdown.
    """
    cumulative = calculate_cumulative_returns(returns)
    total_return = cumulative.iloc[-1] - 1
    
    # Annualize (assuming 252 trading days)
    ann_return = (1 + total_return) ** (252 / len(returns)) - 1
    
    # Sharpe Ratio
    vol = returns.std() * np.sqrt(252)
    sharpe = (ann_return - risk_free_rate) / vol
    
    # Max Drawdown
    max_dd = calculate_drawdown(cumulative)
    
    return {
        "Total Return": f"{total_return:.2%}",
        "Annualized Return": f"{ann_return:.2%}",
        "Sharpe Ratio": f"{sharpe:.2f}",
        "Max Drawdown": f"{max_dd:.2%}"
    }