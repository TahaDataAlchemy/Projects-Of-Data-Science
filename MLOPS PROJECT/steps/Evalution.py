import pandas as pd
import logging
from zenml import step

from src.Evaluation import MSE, R2,RMSE
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated

@step
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

        r2_class = R2()
        r2 = r2_class.calculate_scores(y_test,prediction)

        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test,prediction)
        return r2,rmse
    except Exception as e:
        logging.error("Error in evaluting model : {}".format(e))
        


