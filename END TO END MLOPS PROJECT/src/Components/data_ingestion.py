import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.append(project_root)

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
import logging
from src.exception import CustomException
from src.Components.data_transformation import DataTransformation
from src.Components.data_transformation import DataTransformationConfig
from src.Components.model_trainer import ModelTrainerConfig
from src.Components.model_trainer import ModelTrainer

@dataclass # Because of this class also called Decorator, we can easily declare our variables without using def __init__ for every variable
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "data.csv")

class DataIngestion:
    """
    We are not using @dataclass decorator as it is good for defining variable but if your class has multiple functionalities then use __init__ method for it
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        # Reading Data from data source
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv(os.path.join(project_root, 'notebook/data/stud.csv'))
            logging.info("Imported data successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train Test Initiated")
            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.error(f"Error occurred during data ingestion: {e}")
            raise CustomException(e, sys)

        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))





