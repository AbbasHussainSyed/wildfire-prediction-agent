
# Wildfire Prediction Agent

This project uses a machine learning model to predict wildfire risk in various regions of the United States. The predictions are based on trained data, allowing the user to interact with the system by providing coordinates (latitude and longitude) and risk values through a user-friendly web interface powered by Gradio.

Features
	•	Fire Risk Prediction: Predict wildfire risk for a given set of latitude, longitude, and risk values.
	•	User Interaction: Use dropdowns to select or modify latitude, longitude, and fire risk values.
	•	Map Visualization: A dynamic map that displays the fire risk predictions in real-time.

Tech Stack
	•	Backend: Python 3.x
	•	Machine Learning: Scikit-learn, TensorFlow (for model training and predictions)
	•	Web Framework: Gradio (for the user interface)
	•	Data Visualization: Folium (for interactive map visualization)
	•	Deployment: Render (for cloud deployment)

Models
	•	The wildfire risk prediction model has been trained using historical fire data (latitude, longitude, and associated fire risk) to detect and predict potential wildfire occurrences in different regions.
	•	The model uses machine learning algorithms to predict fire risk levels based on geographical coordinates and historical risk data.

Installation

Prerequisites
	•	Python 3.x
	•	pip
	•	Virtual environment (optional but recommended)

1. Clone the repository

Clone the repository to your local machine.

git clone https://github.com/AbbasHussainSyed/wildfire-prediction-agent.git
cd wildfire-prediction-agent

2. Create a virtual environment (optional)

You can create a virtual environment to keep your dependencies isolated.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies

Install the required Python dependencies using pip:

pip install -r requirements.txt

4. Run the application

To run the application locally, execute the following:

python src/fire_risk_map_app.py

This will start the application on a local server. You can access the app by visiting http://127.0.0.1:5000/ in your web browser.

Usage
	1.	Launch the web app: Open your browser and go to the provided localhost URL.
	2.	Interact with the app: Select latitude, longitude, and risk from the dropdown menus.
	3.	View predictions: The app will display the predicted fire risk on a map, based on the provided values.

Folder Structure

    wildfire-prediction-agent/
    ├── src/
    │   ├── fire_risk_map_app.py   # Main script that runs the app
    │   ├── model/                 # Contains trained model files
    ├── requirements.txt           # List of dependencies
    └── render.yaml                # Render configuration file (for deployment)

Deployment on Render
	1.	Deploy on Render: You can deploy the application on Render by following the steps mentioned in the Render Deployment Docs.
	2.	Configuration: Add the render.yaml file to the root of your repository to specify the deployment settings.

Notes
	•	Model Training: The model used for fire risk prediction has been trained with historical fire data. The purpose of this training is to enable the app to predict the risk of wildfire based on past trends.
	•	Fire Risk Data: The prediction is made based on historical patterns of fire occurrences, the latitude, longitude, and current risk levels.

License

This project is licensed under the MIT License - see the LICENSE file for details.
