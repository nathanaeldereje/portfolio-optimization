import pytest
import pandas as pd
import numpy as np

def test_pandas_environment():
    """
    Simple smoke test to ensure pandas is installed 
    and can create a DataFrame (essential for Task 1).
    """
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Price': [100, 102, 101, 105, 107]
    }
    df = pd.DataFrame(data)
    
    assert not df.empty
    assert len(df) == 5
    assert 'Price' in df.columns

def test_return_calculation():
    """
    Test a simple calculation logic relevant to the project 
    (Daily Returns) to ensure numpy/pandas math works.
    """
    prices = pd.Series([100, 110, 121])
    # Expected return: (110-100)/100 = 0.1, (121-110)/110 = 0.1
    returns = prices.pct_change().dropna()
    
    expected_return = 0.1
    
    # Check if calculated return matches expected within a tolerance
    assert np.isclose(returns.iloc[0], expected_return)
    assert np.isclose(returns.iloc[1], expected_return)

if __name__ == "__main__":
    pytest.main()