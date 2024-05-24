import pandas as pd
import logging
from zenml import step

@step
def train_model(df: pd.DataFrame) -> None:
    """
    Trains the model on the ingested data

    Args
    df: the ingested Data
    """