import folium
import pandas as pd

def generate_fire_map(predictions_path="predictions.csv"):
    df = pd.read_csv(predictions_path)
    california_map = folium.Map(location=[36.7783, -119.4179], zoom_start=6)
    
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=row["risk"] * 10,
            color="red" if row["risk"] > 0.7 else "orange",
            fill=True,
            tooltip=f"Risk: {row['risk']:.2f}"
        ).add_to(california_map)
    
    california_map.save("output/fire_risk_map.html")