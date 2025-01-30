import folium
import pandas as pd
import os


def generate_fire_map(
    predictions_path="/Users/abbassyed/Coding_Projects/wildfire-prediction-agent/wildfire-prediction-agent/src/predictions.csv",):
    if not os.path.exists(predictions_path):
        print(f"File {predictions_path} not found!")
        return

    df = pd.read_csv(predictions_path)
    print(f"Data loaded. Number of rows: {len(df)}")

    california_map = folium.Map(location=[36.7783, -119.4179], zoom_start=6)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=row["risk"] * 10,
            color="red" if row["risk"] > 0.7 else "orange",
            fill=True,
            tooltip=f"Risk: {row['risk']:.2f}",
        ).add_to(california_map)

    save_path = "fire_risk_map.html"
    california_map.save(save_path)
    print(f"Map saved to {save_path}")


generate_fire_map()
