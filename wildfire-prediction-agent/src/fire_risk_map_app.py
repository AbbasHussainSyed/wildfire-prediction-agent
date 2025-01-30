import gradio as gr
import folium
from folium.plugins import MarkerCluster

# Sample data: latitude, longitude, and risk values
data = [
    {"latitude": 34.0522, "longitude": -118.2437, "risk": 0.85},
    {"latitude": 36.7783, "longitude": -119.4179, "risk": 0.65},
    {"latitude": 37.7749, "longitude": -122.4194, "risk": 0.45},
    {"latitude": 33.8688, "longitude": -117.1235, "risk": 0.9},
    {"latitude": 35.6867, "longitude": -120.5872, "risk": 0.6},
]


# Function to map latitude and longitude to the corresponding risk value
def get_risk(lat, lon):
    for entry in data:
        if entry["latitude"] == lat and entry["longitude"] == lon:
            return entry["risk"]
    return "No data"


# Function to create and display the map
def create_map(lat, lon):
    # Create a folium map centered on the average latitude and longitude
    m = folium.Map(location=[lat, lon], zoom_start=6)

    # Add a marker cluster for risk points
    marker_cluster = MarkerCluster().add_to(m)

    # Add points to the map
    for entry in data:
        folium.Marker(
            location=[entry["latitude"], entry["longitude"]],
            popup=f"Risk: {entry['risk']}",
            icon=folium.Icon(color="red" if entry["risk"] > 0.7 else "blue"),
        ).add_to(marker_cluster)

    # Return the map as an HTML string
    map_html = m._repr_html_()  # Get HTML representation of the folium map
    return map_html


# Gradio interface function
def gradio_interface(lat, lon):
    risk = get_risk(lat, lon)
    map_html = create_map(lat, lon)
    return map_html, f"Latitude: {lat}, Longitude: {lon}, Risk: {risk}"


# Create Sliders for latitude and longitude
latitude_slider = gr.Slider(
    minimum=24.396308,
    maximum=49.384358,
    value=37.7749,
    label="Latitude (United States)",
    step=0.01,
)
longitude_slider = gr.Slider(
    minimum=-125.0,
    maximum=-66.93457,
    value=-122.4194,
    label="Longitude (United States)",
    step=0.01,
)

risk_display = gr.Textbox(label="Risk Level")

# Create the Gradio interface with Sliders
iface = gr.Interface(
    fn=gradio_interface,
    inputs=[latitude_slider, longitude_slider],
    outputs=[gr.HTML(label="Map"), risk_display],
)

# Launch the interface
iface.launch()
