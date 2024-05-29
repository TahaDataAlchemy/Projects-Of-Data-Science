import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error , r2_score

class Evalution(ABC):
    @abstractmethod
    def calculate_scores(self,y_true:np.ndarray,y_pred:np.ndarray):
        """
        calculates the scores for the model

        Args:
            y_true: mean actual variable y_test
            y_pred: model.predict(X_test)

            return None
        """
        pass

class MSE(Evalution):
    """
    Evalution strategy that uses Mean Squared Error
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true,y_pred)
            logging.info("MSE. {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating MSE: {}".format(e))
            raise e
        
class R2(Evalution):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating RMSE")
            r2 = r2_score(y_true, y_pred)
            logging.info("RMSE. {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e 
        
        
class RMSE(Evalution):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating RMSE")
            rmse = mean_squared_error(y_true, y_pred,squared=False)
            logging.info("RMSE. {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e 