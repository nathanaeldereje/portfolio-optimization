Here is the updated **notebooks/README.md**. I have adjusted the numbering to reflect that **Task 3 (Future Forecasting)** now has its own dedicated notebook, shifting the Portfolio Optimization and Backtesting notebooks to 04 and 05.

---

# 📓 Analysis Notebooks

This directory contains the Jupyter Notebooks used for the step-by-step analysis, modeling, and optimization of the GMF Investment strategy.

## 📂 Notebook Directory

| Order | Notebook Name | Description | Key Tasks & Outputs |
| :--- | :--- | :--- | :--- |
| **01** | `01_eda_preprocessing.ipynb` | **Data Extraction & EDA**<br>Fetches data from YFinance, cleans it, and analyzes statistical properties. | • Fetch TSLA, BND, SPY<br>• Stationarity Tests (ADF)<br>• Outlier Detection & Volatility Analysis |
| **02** | `02_ts_forecasting.ipynb` | **Time Series Modeling**<br>Develops and compares statistical and deep learning models for TSLA. | • ARIMA vs LSTM Comparison<br>• Model Evaluation (MAE/RMSE/MAPE)<br>• Selection of Best Model (LSTM) |
| **03** | `03_future_forecasting.ipynb` | **Future Trend Analysis**<br>Uses the trained LSTM to project future prices with uncertainty bounds. | • Recursive Multi-step Forecast<br>• Confidence Intervals (Fan Chart)<br>• Opportunity & Risk Assessment |
| **04** | `04_portfolio_optimization.ipynb` | **Portfolio Construction (MPT)**<br>Uses forecasted returns to build an optimized portfolio. | • Covariance Matrix Heatmap<br>• Efficient Frontier Generation<br>• Max Sharpe & Min Volatility Weights |
| **05** | `05_backtesting.ipynb` | **Strategy Validation**<br>Simulates portfolio performance against a standard benchmark. | • Cumulative Returns Plot<br>• Comparison vs. 60/40 Benchmark<br>• Risk Metrics (Drawdown, Alpha) |

## 🛠️ Setup & Usage

To ensure imports from the `src/` module work correctly, each notebook includes a path injection block at the top.

**Standard Import Block:**
At the top of each notebook, you will see:
```python
import sys
import os

# Add the parent directory to sys.path to access src/
sys.path.append(os.path.abspath(os.path.join('..')))

# Example import from custom modules
from src.forecasting import calculate_metrics, create_sequences
```
