# src/preprocess.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from config.settings import PROCESSED_DATA_DIR


def preprocess_data():
    # Load raw datasets
    fire_df = pd.read_csv("data/raw/fire_data.csv")
    weather_df = pd.read_csv("data/raw/weather_data.csv")

    # Convert date to datetime
    fire_df["date"] = pd.to_datetime(fire_df["date"])
    weather_df["date"] = pd.to_datetime(weather_df["date"])

    # Merge datasets on date
    merged_df = pd.merge(fire_df, weather_df, on="date", how="inner")

    # Drop duplicates
    merged_df = merged_df.drop_duplicates(subset=["date"])

    # Normalize numerical features
    scaler = MinMaxScaler()
    cols_to_scale = ["temp", "humidity", "wind_speed", "frp"]
    cols_to_scale = ["temp", "humidity", "wind_speed", "month"]

    # Remove missing columns dynamically
    cols_to_scale = [col for col in cols_to_scale if col in merged_df.columns]

    if not cols_to_scale:
        raise ValueError("No valid columns found for scaling!")

    # Apply scaling
    merged_df[cols_to_scale] = scaler.fit_transform(merged_df[cols_to_scale])

    # Create lag features for LSTM
    for lag in range(1, 4):
        merged_df[f"frp_lag_{lag}"] = merged_df["frp"].shift(lag)

    # Handle missing values
    merged_df.fillna(method="ffill", inplace=True)

    # Save processed data
    merged_df.to_csv(f"{PROCESSED_DATA_DIR}/merged_dataset.csv", index=False)

    return merged_df


if __name__ == "__main__":
    preprocess_data()
