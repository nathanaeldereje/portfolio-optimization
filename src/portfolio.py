# src/portfolio.py
import pandas as pd
import numpy as np
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

def get_expected_returns(adj_close_df, tsla_forecast_df):
    """
    Calculates annualized expected returns: 
    - Historical for BND and SPY
    - Forecast-based for TSLA
    """
    # 1. Historical returns for all (as baseline)
    mu = expected_returns.mean_historical_return(adj_close_df)
    
    # 2. Update TSLA with Forecasted Return
    current_price = adj_close_df['TSLA'].iloc[-1]
    future_price = tsla_forecast_df['Forecast'].iloc[-1]
    forecast_days = len(tsla_forecast_df)
    
    # Annualize the forecast return
    tsla_total_return = (future_price / current_price) - 1
    tsla_ann_return = (1 + tsla_total_return) ** (252 / forecast_days) - 1
    
    mu['TSLA'] = tsla_ann_return
    return mu

def get_covariance_matrix(adj_close_df):
    """Calculates the sample covariance matrix."""
    return risk_models.sample_cov(adj_close_df)

def optimize_portfolio(mu, S, criterion='max_sharpe'):
    """
    Optimizes weights based on either 'max_sharpe' or 'min_volatility'.
    """
    ef = EfficientFrontier(mu, S)
    
    if criterion == 'max_sharpe':
        weights = ef.max_sharpe()
    else:
        weights = ef.min_volatility()
        
    cleaned_weights = ef.clean_weights()
    performance = ef.portfolio_performance(verbose=False)
    
    return cleaned_weights, performance