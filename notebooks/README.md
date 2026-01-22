# 📓 Analysis Notebooks

This directory contains the Jupyter Notebooks used for the step-by-step analysis, modeling, and optimization of the GMF Investment strategy.

## 📂 Notebook Directory

| Order | Notebook Name | Description | Key Tasks & Outputs |
| :--- | :--- | :--- | :--- |
| **01** | `01_eda_preprocessing.ipynb` | **Data Extraction & Exploratory Analysis**<br>Fetches data from YFinance, cleans it, and analyzes statistical properties. | • Fetch TSLA, BND, SPY<br>• Stationarity Tests (ADF)<br>• Decomposition & Volatility Plots |
| **02** | `02_ts_forecasting.ipynb` | **Time Series Modeling**<br>Develops and compares statistical and deep learning models to predict TSLA prices. | • ARIMA/SARIMA Implementation<br>• LSTM Network Training<br>• Model Comparison (MAE/RMSE)<br>• 6-12 Month Forecast |
| **03** | `03_portfolio_optimization.ipynb` | **Portfolio Construction (MPT)**<br>Uses forecasted returns to build an optimized portfolio on the Efficient Frontier. | • Covariance Matrix Calculation<br>• Efficient Frontier Plot<br>• Max Sharpe & Min Volatility Weights |
| **04** | `04_backtesting.ipynb` | **Strategy Validation**<br>Simulates the recommended portfolio performance against a standard benchmark. | • Cumulative Returns Plot<br>• Comparison vs. 60/40 Benchmark<br>• Risk Metrics (Drawdown, Alpha) |

## 🛠️ Setup & Usage

To ensure imports from the `src/` module work correctly, the notebooks are configured to look for local modules.

**Standard Import Block:**
At the top of each notebook, you will see:
```python
import sys
import os

# Add the parent directory to sys.path to access src/
sys.path.append(os.path.abspath('..'))

from src import data_loader, processing