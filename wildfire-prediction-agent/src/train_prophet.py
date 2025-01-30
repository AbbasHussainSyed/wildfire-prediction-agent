# src/train_prophet.py
from prophet import Prophet
import joblib
import pandas as pd
import os
from config.settings import PROCESSED_DATA_DIR


def train_prophet_model():
    print("Starting to train Prophet model...")

    # Load and prepare data
    df = pd.read_csv(f"{PROCESSED_DATA_DIR}/merged_dataset.csv")

    # Ensure date column is in datetime format
    df["date"] = pd.to_datetime(df["date"])

    # Prepare dataset for Prophet
    prophet_df = df[["date", "frp"]].rename(columns={"date": "ds", "frp": "y"})

    # Initialize and train Prophet model
    model = Prophet(seasonality_mode="multiplicative")
    model.add_seasonality(name="monthly", period=30.5, fourier_order=5)
    print("Fitting the model with data...")
    model.fit(prophet_df)

    # Ensure the 'models' directory exists
    os.makedirs("models", exist_ok=True)

    # Save the trained model
    model_path = "models/prophet_model.pkl"
    print(f"Saving model to {model_path}...")
    joblib.dump(model, model_path)

    print("Model training and saving complete.")
    return model


if __name__ == "__main__":
    train_prophet_model()
