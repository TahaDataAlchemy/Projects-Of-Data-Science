import numpy as np
import pandas as pd
from zenml import pipeline,step
from zenml.config import DockerSettings

from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW, TENSORFLOW
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)
from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from zenml.steps import BaseParameters, Output

docker_settings = DockerSettings(required_integrations=[MLFLOW])

from steps.CleanData import clean_df
from steps.Evalution import evaluate_model
from steps.data_ingestion import ingest_df
from steps.model_train import train_model
from zenml.steps import BaseParameters,Output

class DeploymentTriggerConfig(BaseParameters):
    """use case:
            only deploy when greater then min_accuracy
            """
    min_accuracy = 0

@step
def deployment_trigger(
    accuracy:float,
    config:DeploymentTriggerConfig
):
    """Implement a simple trigger that looks at min accuracy and decide whether to deploy or not"""
    return accuracy>=config.min_accuracy

class MLFlowDeploymentLoaderStepParameters(BaseParameters):
    """Get the prediction service started by the deployment pipeline.

    Args:
        pipeline_name: name of the pipeline that deployed the MLflow prediction
            server
        step_name: the name of the step that deployed the MLflow prediction
            server
        running: when this flag is set, the step only returns a running service
        model_name: the name of the model that is deployed
    """
    pipeline_name :str
    step_name: str
    running: bool

@pipeline(enable_cache=False,settings={"docker":docker_settings})
def continuous_deployment_pipeline(
    data_path: str,
    min_accuracy: float = 0,
    #Worker is used that if multiple request sends on a web deployed model it will handle by the number of declared workers means if it return 1 then it will handle one request at a time if 4 then it will handle four request simultaneously
    workers: int = 1,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    df = ingest_df(data_path = data_path)
    X_train,X_test,y_train,y_test = clean_df(df) 
    model = train_model(X_train,X_test,y_train,y_test)
    r2_score,rmse = evaluate_model(model,X_test,y_test)
    deployment_decision = deployment_trigger(rmse)
    mlflow_model_deployer_step(
        model = model,
        deploy_decision = deployment_decision,
        workers = workers,
        timeout = timeout,
    )
@pipeline(enable_cache=False, settings={"docker": docker_settings})
def inference_pipeline(pipeline_name: str, pipeline_step_name: str):
    pass