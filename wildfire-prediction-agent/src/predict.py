import joblib
import torch


def predict_risk(lat, lon, date, model_type):
    """
    Predict wildfire risk using either Prophet or LSTM models.

    Parameters:
        lat (float): Latitude.
        lon (float): Longitude.
        date (str): Date in 'YYYY-MM-DD' format.
        model_type (str): The type of model ('prophet' or 'lstm').

    Returns:
        float: Predicted risk score.
    """
    if model_type == "prophet":
        # Load Prophet model
        prophet_model = joblib.load("models/prophet_model.pkl")
        # Simulate prediction logic (replace with your own)
        prediction = prophet_model.predict([[lat, lon]])
        return prediction[0]

    elif model_type == "lstm":
        # Load LSTM model
        lstm_model = torch.load("models/lstm_model.pt")
        lstm_model.eval()
        # Simulate prediction logic (replace with your own)
        input_tensor = torch.tensor([[lat, lon]], dtype=torch.float32)
        prediction = lstm_model(input_tensor)
        return prediction.item()

    else:
        raise ValueError("Invalid model_type. Choose 'prophet' or 'lstm'.")
