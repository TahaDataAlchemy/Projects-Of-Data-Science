import logging

import pandas as pd
from src.dataCleaning import DataCleaning, DataPreprocessStrategy


def get_data_for_test():
    try:
        df = pd.read_csv("C:\Users\Pc\Desktop\Taha\Projects-Of-Data-Science\MLOPS PROJECT\data\olist_customers_dataset.csv")
        df = df.sample(n=100)
        preprocess_strategy = DataPreprocessStrategy()
        data_cleaning = DataCleaning(df, preprocess_strategy)
        df = data_cleaning.handle_data()
        df.drop(["review_score"], axis=1, inplace=True)
        result = df.to_json(orient="split")
        return result
    except Exception as e:
        logging.error(e)
        raise e
