import gradio as gr
import joblib
import torch
from src.predict import predict_risk
from src.visualize import generate_fire_map

def gradio_interface(lat, lon, date):
    # Predict using both models
    prophet_risk = predict_risk(lat, lon, date, model_type="prophet")
    lstm_risk = predict_risk(lat, lon, date, model_type="lstm")
    
    # Generate map
    generate_fire_map()
    
    return {
        "prophet_risk": prophet_risk,
        "lstm_risk": lstm_risk,
        "map": "output/fire_risk_map.html"
    }

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Number(label="Latitude", precision=4),
        gr.Number(label="Longitude", precision=4),
        gr.Textbox(label="Date (YYYY-MM-DD)")
    ],
    outputs=[
        gr.Label(label="Prophet Prediction"),
        gr.Label(label="LSTM Prediction"),
        gr.HTML(label="Risk Map")
    ],
    title="🔥 Wildfire Prediction System",
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()