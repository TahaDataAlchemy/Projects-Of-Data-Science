**Data Ingestion Module**

    The DataIngestion module is designed to facilitate the process of reading raw data from a source, processing it, and saving it in a structured format for further analysis and machine learning tasks. The module leverages pandas for data manipulation and logging for tracking the ingestion process. This module is a critical part of any data pipeline, ensuring that data is correctly loaded and split into training and testing sets.

**Key Components**

**1. DataIngestionConfig**

    @dataclass is a decorator, we don't need to put init again and again for just declaring variables.

    A configuration class using the @dataclass decorator to define paths for the training, testing, and raw data files.

    Attributes:
    1) train_data_path: Path to save the training data.
    2) test_data_path: Path to save the testing data.
    3) raw_data_path: Path to save the raw data.

**DataIngestion**

    A class responsible for the ingestion of data from a source and its preparation for machine learning tasks.

    1) First, we are reading data from the source; it can be any source like Hadoop, database.

    2) As we make an artifact directory, my train and test files will be saved there. It is useful because if the data pipeline crashes, we have our data locally available. Another purpose is that when I split data into train and test, it will save these datasets in a separate folder to be used for further procedures.

    3) After splitting, saving it to the artifact folder.

    4) Returning data paths for train and test data because they will be used in the data_transformation class.

    5) Saving raw data also because if we need to change the train or test data, then it will work for us. If the pipeline crashes or needs to be restarted, the raw data is already saved and does not need to be ingested again from the original source.



**Data Transformation Module**

    This script is designed to handle data transformation for a machine learning project. It reads train and test datasets, preprocesses the data using pipelines for numerical and categorical features, and saves the preprocessing object for future use. The script is modular and handles exceptions gracefully.


**Key Components**

**DataTransformationConfig**

    A configuration class using the @dataclass decorator to define the path for the preprocessor object file.

**Attributes:**

    preprocessor_obj_file_path: Path to save the preprocessor object.

**DataTransformation**

    1) A class responsible for the transformation of data for machine learning tasks.

**Methods:**
    __init__:

        Initializes the DataTransformation class with a configuration for saving the preprocessor object.

**get_data_transformer_object:**

    Purpose: Creates and returns a ColumnTransformer object for preprocessing numerical and categorical data.
    
    Steps:
    
    1) Defines numerical and categorical columns.
    2) Creates a numerical pipeline with imputation (median strategy) and scaling.
    3) Creates a categorical pipeline with imputation (most frequent strategy), one-hot encoding, and scaling.
    4) Combines both pipelines into a ColumnTransformer.
    5) Logs the completion of scaling for both numerical and categorical columns.
    6) Returns the ColumnTransformer object.

**initiate_data_transformation:**

    Purpose: Reads train and test datasets, applies the preprocessing pipelines, and saves the preprocessor object.
    
    Steps:
    
    1) Reads the train and test datasets from specified paths.
    2) Logs the completion of reading data.
    3) Obtains the preprocessing object using get_data_transformer_object.
    4) Defines the target column and the feature columns.
    5) Splits the train and test datasets into input features and target features.
    6) Applies the preprocessing object on the input features.
    7) Concatenates the processed input features with the target features.
    8) Logs the application of the preprocessing object.
    9) Saves the preprocessing object using save_object.
    10) Saving Code is written on Utils File purpose of it is to save the file in the pickle format
    11) Returns the processed train and test arrays along with the path to the saved preprocessor object.


**Model Trainer Module**

