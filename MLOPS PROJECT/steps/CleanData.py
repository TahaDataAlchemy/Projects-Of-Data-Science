import logging
import pandas as pd
from zenml import step
from src.dataCleaning import DataCleaning, DataDividingStrategy,DataPreProcessingStrategy
from typing_extensions import Annotated
from typing import Tuple



@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame,"X_train"],
    Annotated[pd.DataFrame,"X_test"],
    Annotated[pd.Series,"y_train"],
    Annotated[pd.Series,"y_test"],
]:
    try:
        processStrategy = DataPreProcessingStrategy()
        data_cleaning = DataCleaning(df, processStrategy)
        processed_data = data_cleaning.handle_data()

        divide_Strategy = DataDividingStrategy()
        data_cleaning = DataCleaning(processed_data, divide_Strategy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data Cleaning Complete")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error in cleaning data {}".format(e))
        raise e