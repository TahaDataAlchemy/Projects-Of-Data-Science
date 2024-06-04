from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__ == "__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri()) # Use for Opening Mlflow server
    train_pipeline(data_path = r"C:\Users\Pc\Desktop\Taha\Projects-Of-Data-Science\MLOPS PROJECT\data\olist_customers_dataset.csv")
    


# pipeline Visulization Commands:
        # mlflow ui --backend-store-uri  "file:C:\Users\Pc\AppData\Roaming\zenml\local_stores\cb74b11f-5df8-4f21-8515-3af5ee40c668\mlruns"
        # zenml --blocking up