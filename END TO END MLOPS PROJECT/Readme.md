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
        The Model Trainer module is designed to facilitate the process of training multiple machine learning models, evaluating their performance, and selecting the best model based on the R² score. The module includes functionalities for saving the best-performing model for future predictions.
    
**Key Components**

**ModelTrainerConfig**

    @dataclass is a decorator, we don't need to put init again and again for just declaring variables.

    A configuration class using the @dataclass decorator to define the path for the trained model file. 
    Attributes:

    trained_model_file_path: Path to save the trained model object.

**ModelTrainer**

    A class responsible for training and evaluating various regression models, and saving the best-performing model.

    Methods:

    init:

    Initializes the ModelTrainer class with a configuration for saving the trained model object.

**initiate_model_trainer**:

    Purpose: Trains multiple regression models on the provided training data, evaluates their performance on the test data, and saves the best-performing model.

    Steps:

    Splits the input data:

    Splits the provided training and test arrays into input features (X) and target variable (y).
    Defines the models:

    Creates a dictionary of regression models to be evaluated, including:
    RandomForestRegressor
    DecisionTreeRegressor
    GradientBoostingRegressor
    LinearRegression
    XGBRegressor
    CatBoostRegressor
    AdaBoostRegressor
    Evaluates the models:

    Uses the evalute_model function to evaluate each model's performance on the training and test datasets.
    Logs the model evaluation process.

**Models and Hyperparameters**
    Random Forest
    Decision Tree
    Gradient Boosting
    Linear Regression
    XGBRegressor
    CatBoosting Regressor
    AdaBoost Regressor
    The hyperparameters for each model are defined in the params dictionary.

**Selects the best model:**

    Identifies the model with the highest R² score from the evaluation results.
    If no model achieves an R² score above 0.60, raises a CustomException.
    Saves the best model:

    Uses the save_object function to save the best-performing model to the specified file path.
    Logs the model saving process.
    Returns the R² score:

    Predicts the target variable for the test data using the best model.
    Calculates and returns the R² score for the predictions.
**Exception Handling**:

    Catches and logs any exceptions that occur during the model training and evaluation process.
    Raises a CustomException with the error message if an exception is encountered.
    This module is essential for training and selecting the best regression model for a given dataset, ensuring that the most accurate model is saved for future predictions. 


**Predicted Pipeline**

        This class is responsible for Predicting Custom Data input by Users  

