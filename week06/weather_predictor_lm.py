import joblib
import pandas as pd
from weather_prediction_lm import clean_format_data_frame

# Load the trained model
model_file = 'ridge_model.joblib'
reg = joblib.load(model_file)

# Prepare new data (example)
weather_data = "week06\palmer_weather_data_2000-2024.csv"

formatted_weather_data = clean_format_data_frame(weather_data)

# Make predictions
predictions = reg.predict(formatted_weather_data)

# Display predictions
print("Predictions:", predictions)