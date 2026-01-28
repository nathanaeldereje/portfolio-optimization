# 📈 Portfolio Management Optimization using Time Series Forecasting
**Project:** Guide Me in Finance (GMF) Investments Strategy  
**Role:** Financial Data Analyst / AI Engineer  
**Status:** ✅ Completed

## Project Overview
This project empowers **Guide Me in Finance (GMF) Investments** to leverage data-driven insights for personalized portfolio management. By integrating advanced time series forecasting with Modern Portfolio Theory (MPT), we aim to optimize asset allocation for clients.

Using historical financial data, the system predicts market trends for high-growth assets (specifically Tesla) and constructs an optimized portfolio balancing high-risk assets, stable bonds, and broad market indices.
**Goal:** Minimize risks and capitalize on market opportunities by transitioning from traditional analysis to predictive modeling and algorithmic optimization.

## 📖 Business Objective
**Guide Me in Finance (GMF)** is a forward-thinking advisory firm. While the Efficient Market Hypothesis suggests exact price prediction is difficult, GMF aims to use advanced modeling to forecast volatility and momentum to gain a competitive edge.

*   **The Problem:** Financial analysts spend excessive time interpreting raw data. Traditional static portfolios may not adapt quickly enough to market volatility or momentum shifts in high-growth sectors.
*   **The Solution:** A robust pipeline that forecasts future stock movements (using ARIMA & LSTM) and mathematically determines the optimal asset weights to maximize returns for a given risk level (Sharpe Ratio).

**Key Performance Indicators (KPIs):**
*   **Forecast Accuracy:** Minimize MAE, RMSE, and MAPE for stock price predictions.
*   **Portfolio Efficiency:** Maximize the Sharpe Ratio of the recommended portfolio.
*   **Risk Management:** Accurately estimate Value at Risk (VaR) and volatility.

## 📊 Data & Assets
The analysis covers the period from **Jan 1, 2015 – Jan 15, 2026** using data from YFinance.

| Asset | Ticker | Role in Portfolio | Risk Profile |
| :--- | :--- | :--- | :--- |
| **Tesla** | `TSLA` | High-growth potential | 🔴 High Risk |
| **Vanguard Total Bond ETF** | `BND` | Stability & Income | 🟢 Low Risk |
| **S&P 500 ETF** | `SPY` | Market Diversification | 🟡 Moderate Risk |

## 📂 Repository Structure
```text
portfolio-optimization/
├── .github/workflows/  # CI/CD for automated testing
├── data/               # Raw and Processed data (Gitignored)
├── notebooks/          # Jupyter Notebooks for EDA, Modeling, and Backtesting
├── scripts/            # Python scripts for data fetching and utils
├── src/                # Source code for modular logic
├── tests/              # Unit tests
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🛠️ Getting Started

### Prerequisites
*   Python 3.9+
*   VS Code or Jupyter Lab

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/portfolio-optimization.git
    cd portfolio-optimization
    ```

2.  **Set up the environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Tests**
    Ensure the environment is set up correctly by running the initial smoke tests:
    ```bash
    pytest
    ```

## 🔄 Recommended Workflow

1.  **Data Extraction & EDA (Task 1)**
    *   Fetch YFinance data for TSLA, BND, and SPY; clean data and analyze statistical properties.
    *   **Run:** `notebooks/01_eda_preprocessing.ipynb`
    *   *Key Output:* Stationarity test results (ADF), Volatility Clustering analysis, and Time Series Decomposition.

2.  **Time Series Modeling (Task 2)**
    *   Develop and compare statistical (ARIMA) vs. Deep Learning (LSTM) models for `TSLA`.
    *   **Run:** `notebooks/02_ts_forecasting.ipynb`
    *   *Key Output:* Model evaluation metrics (MAE/RMSE/MAPE) and selection of LSTM as the superior model.

3.  **Future Trend Analysis (Task 3)**
    *   Use the trained LSTM model to project future prices with uncertainty bounds.
    *   **Run:** `notebooks/03_future_forecasting.ipynb`
    *   *Key Output:* 6-month recursive price forecast with "Fan Chart" confidence intervals.

4.  **Portfolio Optimization (Task 4)**
    *   Construct the Efficient Frontier using forecasted returns for TSLA and historical returns for BND/SPY.
    *   **Run:** `notebooks/04_portfolio_optimization.ipynb`
    *   *Key Output:* Asset Covariance Heatmap and Optimal weights (e.g., 100% SPY allocation for Max Sharpe).

5.  **Strategy Backtesting (Task 5)**
    *   Simulate the recommended strategy against a static benchmark (60/40 Split) over the last 12 months.
    *   **Run:** `notebooks/05_backtesting.ipynb`
    *   *Key Output:* Cumulative Return vs. Benchmark comparison plot and Risk/Return metrics (Sharpe Ratio, Max Drawdown).

## 🚀 Project Progress & Roadmap

| Phase | Task Description | Status |
| :--- | :--- | :--- |
| **0. Setup** | Project Structure, Git, CI/CD, and Environment Setup | ✅ Completed |
| **1. Explore** | Data Fetching (YFinance), Preprocessing, EDA, Stationarity Tests | ✅ Completed |
| **2. Model** | ARIMA & LSTM implementation, Hyperparameter tuning, Evaluation | ✅ Completed |
| **3. Forecast** | Generating future market trends with confidence intervals | ✅ Completed |
| **4. Optimize** | Modern Portfolio Theory (MPT), Efficient Frontier, Sharpe Ratio | ✅ Completed |
| **5. Validate** | Backtesting strategy against standard market benchmarks | ✅ Completed |

---
*Date: January 27,2026*
