import pandas as pd
import logging
from zenml import step

from src.Evaluation import MSE, R2,RMSE
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated

import mlflow

from zenml.client import Client 

# Use to track the every run of model you initiate to see how it performing in 1st run and in 100th run or what so ever
experiment_tracker = Client().active_stack.experiment_tracker


@step(experiment_tracker=experiment_tracker.name)
def evaluate_model(model: RegressorMixin,
                   X_test: pd.DataFrame,
                   y_test: pd.DataFrame,) -> Tuple[
                       Annotated[float,"r2score"],
                       Annotated[float,"RMSE"],
]:
    try:
        """
        Evaluate the model on ingested data

        Args:
            df: the ingested data
        
        """
        prediction = model.predict(X_test)
        mse_class = MSE()
        mse = mse_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("mse",mse)

        r2_class = R2()
        r2 = r2_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("R2",r2)


        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("rmse",rmse)

        return r2,rmse
    except Exception as e:
        logging.error("Error in evaluting model : {}".format(e))
        


