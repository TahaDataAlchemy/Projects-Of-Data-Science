from zenml import pipeline
from steps.CleanData import clean_df
from steps.Evalution import evaluate_model
from steps.data_ingestion import ingest_df
from steps.model_train import train_model

@pipeline(enable_cache=False)
#CACHE FALSE KA FAIDA YE HAI K AB AGAR CODE ME KOI CHANGES NHI HAI OR DATA ME KOI CHANGES NHI HAI TU WO PEECHLI WALI EXECUTION KO REFER KARKE CHALE GA


def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    X_train,X_test,y_train,y_test = clean_df(df) 
    model = train_model(X_train,X_test,y_train,y_test)
    r2_score,rmse = evaluate_model(model,X_test,y_test)