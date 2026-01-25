# src/loader.py
import yfinance as yf
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self, tickers: list) -> pd.DataFrame:
        """
        Fetches data with a fallback to mock data if the API fails.
        """
        print(f"Fetching data for {tickers} from {self.start_date} to {self.end_date}...")
        
        try:
            # Attempt to download with threads=False to avoid database locks
            data = yf.download(tickers, start=self.start_date, end=self.end_date, group_by='ticker', threads=False)
            
            # Check if data is valid (must have rows and expected columns)
            if not data.empty:
                # Basic check to see if we have multi-level columns (Ticker, Price Info)
                if isinstance(data.columns, pd.MultiIndex):
                    print("Data successfully fetched from API.")
                    return data
                # If single ticker, yfinance might return flat columns, normalize it
                elif len(tickers) == 1:
                    # Reformating for consistency if needed, but usually group_by handles it
                    pass
            
            print("API returned empty or malformed data.")
            raise ValueError("API Data Empty")

        except Exception as e:
            print(f"Warning: API download failed ({e}).")
            print("---------------------------------------------------")
            print("⚠️  SWITCHING TO MOCK DATA MODE")
            print("    (This allows you to proceed with the project)")
            print("---------------------------------------------------")
            return self.generate_mock_data(tickers)

    def generate_mock_data(self, tickers: list) -> pd.DataFrame:
        """
        Generates synthetic financial data for testing pipelines when API is down.
        """
        # Create date range
        dates = pd.date_range(start=self.start_date, end=self.end_date, freq='B') # Business days
        
        # Define attributes usually returned by yfinance
        attributes = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        
        # Create MultiIndex: (Ticker, Attribute)
        columns = pd.MultiIndex.from_product([tickers, attributes], names=['Ticker', 'Price'])
        
        mock_df = pd.DataFrame(index=dates, columns=columns)
        
        for ticker in tickers:
            # Set realistic seed values
            if ticker == 'TSLA':
                start_price, volatility = 200, 0.03 # High volatility
            elif ticker == 'BND':
                start_price, volatility = 80, 0.005 # Low volatility
            elif ticker == 'SPY':
                start_price, volatility = 400, 0.01 # Medium volatility
            else:
                start_price, volatility = 100, 0.015

            # Generate Random Walk for prices
            # np.random.seed(42) # Optional: Fixed seed for reproducibility
            returns = np.random.normal(loc=0.0005, scale=volatility, size=len(dates))
            price_series = start_price * (1 + returns).cumprod()
            
            # Populate DataFrame
            mock_df[(ticker, 'Close')] = price_series
            mock_df[(ticker, 'Adj Close')] = price_series
            mock_df[(ticker, 'Open')] = price_series * 0.99
            mock_df[(ticker, 'High')] = price_series * 1.02
            mock_df[(ticker, 'Low')] = price_series * 0.98
            mock_df[(ticker, 'Volume')] = np.random.randint(1000000, 50000000, size=len(dates))
            
        print("Mock Data Generated Successfully.")
        return mock_df