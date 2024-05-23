import logging
from zenml import steps
import pandas as pd

class IngestData:
    def __init__(self,datapath: str):
        self.data_path = datapath

    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)
