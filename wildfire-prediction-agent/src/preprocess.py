# src/preprocess.py
import pandas as pd
from config.settings import PROCESSED_DATA_DIR


def preprocess_data():
    # Load your existing CSVs
    fire_df = pd.read_csv("data/raw/fire_data.csv")
    weather_df = pd.read_csv("data/raw/weather_data.csv")

    # Merge on date and/or location columns
    # Example: If both datasets have a "date" column
    merged_df = pd.merge(
        fire_df,
        weather_df,
        on="date",  # Adjust to your actual column name
        how="inner",  # Or "left" depending on your use case
    )

    # Save merged data
    merged_df.to_csv(f"{PROCESSED_DATA_DIR}/merged_dataset.csv", index=False)
    return merged_df


if __name__ == "__main__":
    preprocess_data()
