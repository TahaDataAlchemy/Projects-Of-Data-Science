import pandas as pd
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from abc import ABC, abstractmethod
from typing import Union


class DataStrategy(ABC):
    """
    Abstract class defining strategy for handling data
    """
    # Purpose of this class 
    """
    By using an abstract base class and abstract methods, you create a flexible system where new data handling strategies can be easily added without modifying existing code. 
    For instance, if you need a new preprocessing technique, 
    you simply create a new class that inherits from DataStrategy and implements the handle_data method.
    """

    @abstractmethod
    def handle_data(self,data: pd.DataFrame) ->Union[pd.DataFrame,pd.Series]:
        pass

class DataPreProcessingStrategy(DataStrategy):
   def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Removes columns which are not required, fills missing values with median average values, and converts the data type to float.
        """
        try:
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp",
                ],
                axis=1,
            )
            data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            # write "No review" in review_comment_message column
            data["review_comment_message"].fillna("No review", inplace=True)

            data = data.select_dtypes(include=[np.number])
            cols_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(cols_to_drop, axis=1)

            return data
        except Exception as e:
            logging.error(e)
            raise e

class DataDividingStrategy(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame,pd.Series]:
        """
        Data Dividing strategy which divide data into train and test data.
        """
        try:
            X = data.drop("review Score",axis = 1)
            y = data["review_score"]
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)

            return X_train,X_test,y_train,y_test
        except Exception as e:
            logging.error(e)
            raise e

class DataCleaning:
    def __init__(self, data: pd.DataFrame,strategy:DataStrategy):
        self.data = data
        self.strategy = strategy
    
    def handle_data(self) -> Union[pd.DataFrame,pd.Series]:
        """
        Handle DATA
        """
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error in handling data: {}".format(e))
            raise e