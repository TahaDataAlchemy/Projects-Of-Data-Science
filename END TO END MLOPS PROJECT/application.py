#use for deployment purpose otherwise all code is same as app.py
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.append(project_root)
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for a home page
@app.route('/')
def index():
    """
    This function is a route handler for the root URL ("/") of the Flask application. It renders the "index.html" template and returns its content as a response.

    Returns:
        A rendered HTML template as a response.
    """
    return render_template('index.html')

@app.route('/predictdata', methods=["GET", "POST"])
def predict_datapoint():
    """
    This function handles the prediction of a single data point.
    It renders the results on the HTML GUI.
    """
    if request.method == 'GET':
        # Render the HTML template for the home page
        return render_template('home.html')
    else:
        # Extract the data from the form
        data = CustomData(
            gender=request.form.get('gender'),  # Gender of the student
            race_ethnicity=request.form.get('ethnicity'),  # Race/Ethnicity of the student
            parental_level_of_education=request.form.get('parental_level_of_education'),  # Parent's level of education
            lunch=request.form.get('lunch'),  # Lunch type
            test_preparation_course=request.form.get('test_preparation_course'),  # Test preparation course
            reading_score=float(request.form.get('writing_score')),  # Reading score
            writing_score=float(request.form.get('reading_score'))  # Writing score
        )
        # Convert the data to a DataFrame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        # Create a prediction pipeline object
        predict_pipeline = PredictPipeline()
        # Predict the math score using the prediction pipeline
        results = predict_pipeline.predict(pred_df)

        # Render the HTML template with the prediction result
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
