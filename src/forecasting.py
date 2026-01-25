import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense, Dropout # type: ignore

def train_test_split_time_series(data, test_size):
    """
    Splits data chronologically.
    """
    train_data = data[:-test_size]
    test_data = data[-test_size:]
    return train_data, test_data

def create_sequences(data, seq_length=60):
    """
    Creates sequences for LSTM [samples, time_steps, features]
    """
    x, y = [], []
    for i in range(seq_length, len(data)):
        x.append(data[i-seq_length:i, 0])
        y.append(data[i, 0])
    return np.array(x), np.array(y)

def build_lstm_model(input_shape, units=50, dropout_rate=0.2):
    """
    Builds and compiles a compiled LSTM model.
    """
    model = Sequential()
    # Layer 1
    model.add(LSTM(units=units, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(dropout_rate))
    # Layer 2
    model.add(LSTM(units=units, return_sequences=False))
    model.add(Dropout(dropout_rate))
    # Output
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def calculate_metrics(y_true, y_pred):
    """
    Calculates MAE, RMSE, and MAPE.
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    # Avoid division by zero
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    return mae, rmse, mape