from prophet import Prophet
import joblib
import pandas as pd
from config.settings import PROCESSED_DATA_DIR

def train_prophet_model():
    df = pd.read_csv(f"{PROCESSED_DATA_DIR}/merged_dataset.csv")
    prophet_df = df[["acq_date", "frp"]].rename(columns={"acq_date": "ds", "frp": "y"})
    
    model = Prophet(
        seasonality_mode="multiplicative",
        yearly_seasonality=8,
        weekly_seasonality=False
    )
    model.fit(prophet_df)
    
    joblib.dump(model, "models/prophet_model.pkl")
    return model