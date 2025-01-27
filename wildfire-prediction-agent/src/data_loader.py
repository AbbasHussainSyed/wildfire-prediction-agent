# src/data_loader.py
import pandas as pd
from config.settings import RAW_DATA_DIR


def load_fire_data():
    """Load fire data from existing CSV"""
    return pd.read_csv(f"{RAW_DATA_DIR}/fire_data.csv")


def load_weather_data():
    """Load weather data from existing CSV"""
    return pd.read_csv(f"{RAW_DATA_DIR}/weather_data.csv")


if __name__ == "__main__":
    # Load data (no API calls needed)
    fire_df = load_fire_data()
    weather_df = load_weather_data()

    # Optional: Save to processed data (if needed)
    fire_df.to_csv(f"{RAW_DATA_DIR}/fire_data.csv", index=False)
    weather_df.to_csv(f"{RAW_DATA_DIR}/weather_data.csv", index=False)
