# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

# NASA FIRMS API (No URL needed - endpoint is hardcoded in data_loader)
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Visual Crossing API
VISUAL_CROSSING_KEY = os.getenv("VISUAL_CROSSING_KEY")

# Paths
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"

