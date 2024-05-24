from zenml import pipeline
from steps.CleanData import clean_df
from steps.Evalution import evaluate_model
from steps.data_ingestion import ingest_df
from steps.model_train import train_model

@pipeline

def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
