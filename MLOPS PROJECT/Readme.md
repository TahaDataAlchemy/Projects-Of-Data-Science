# Predicting how a customer will feel about a product before they even ordered it


### Problem statement: For a given customer's historical data, we are tasked to predict the review score for the next order or purchase. We will be using the Brazilian E-Commerce Public Dataset by Olist. This dataset has information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow viewing charges from various dimensions: from order status, price, payment, freight performance to customer location, product attributes and finally, reviews written by customers. The objective here is to predict the customer satisfaction score for a given order based on features like order status, price, payment, etc. In order to achieve this in a real-world scenario, we will be using ZenML to build a production-ready pipeline to predict the customer satisfaction score for the next order or purchase.

The purpose of this repository is to demonstrate how ZenML empowers your business to build and deploy machine learning pipelines in a multitude of ways:

By offering you a framework and template to base your own work on.
By integrating with tools like MLflow for deployment, tracking and more
By allowing you to build and deploy your machine learning pipelines easily

# Python Requirements

pip install zenml["server"]
zenml up
zenml integration install mlflow -y
zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow --flavor=mlflow
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set

# THE SOLUTION

In order to build a real-world workflow for predicting the customer satisfaction score for the next order or purchase (which will help make better decisions), it is not enough to just train the model once.

Instead, we are building an end-to-end pipeline for continuously predicting and deploying the machine learning model, alongside a data application that utilizes the latest deployed model for the business to consume.

This pipeline can be deployed to the cloud, scale up according to our needs, and ensure that we track the parameters and data that flow through every pipeline that runs. It includes raw data input, features, results, the machine learning model and model parameters, and prediction outputs. ZenML helps us to build such a pipeline in a simple, yet powerful, way.

In this Project, we give special consideration to the MLflow integration of ZenML. In particular, we utilize MLflow tracking to track our metrics and parameters, and MLflow deployment to deploy our model. We also use Streamlit to showcase how this model will be used in a real-world setting.

## Training Pipeline

Our standard training pipeline consists of several steps:

ingest_data: This step will ingest the data and create a DataFrame.
clean_data: This step will clean the data and remove the unwanted columns.
train_model: This step will train the model and save the model using MLflow autologging.
evaluation: This step will evaluate the model and save the metrics -- using MLflow autologging -- into the artifact store.

# Deployment Pipeline
We have another pipeline, the deployment_pipeline.py, that extends the training pipeline, and implements a continuous deployment workflow. It ingests and processes input data, trains a model and then (re)deploys the prediction server that serves the model if it meets our evaluation criteria. The criteria that we have chosen is a configurable threshold on the MSE of the training. The first four steps of the pipeline are the same as above, but we have added the following additional ones:

deployment_trigger: The step checks whether the newly trained model meets the criteria set for deployment.
model_deployer: This step deploys the model as a service using MLflow (if deployment criteria is met).
In the deployment pipeline, ZenML's MLflow tracking integration is used for logging the hyperparameter values and the trained model itself and the model evaluation metrics -- as MLflow experiment tracking artifacts -- into the local MLflow backend. This pipeline also launches a local MLflow deployment server to serve the latest MLflow model if its accuracy is above a configured threshold.

The MLflow deployment server runs locally as a daemon process that will continue to run in the background after the example execution is complete. When a new pipeline is run which produces a model that passes the accuracy threshold validation, the pipeline automatically updates the currently running MLflow deployment server to serve the new model instead of the old one.

While this ZenML Project trains and deploys a model locally, other ZenML integrations such as the Seldon deployer can also be used in a similar manner to deploy the model in a more production setting (such as on a Kubernetes cluster). We use MLflow here for the convenience of its local deployment.

![image](https://github.com/TahaDataAlchemy/Projects-Of-Data-Science/assets/157484236/4a4852a6-b5a6-41b6-a766-74b2daae4830)



