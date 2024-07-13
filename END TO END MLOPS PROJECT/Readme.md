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

