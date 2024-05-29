import logging
from zenml import step
import pandas as pd

class IngestData:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)
    

@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingesting Data from the path

    Args:
        data_path: path to data
    
    Returns:
        DataFrame
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e
