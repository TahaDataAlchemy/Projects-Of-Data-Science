***Data Ingestion Module***
The DataIngestion module is designed to facilitate the process of reading raw data from a source, processing it, and saving it in a structured format for further analysis and machine learning tasks. The module leverages pandas for data manipulation and logging for tracking the ingestion process. This module is a critical part of any data pipeline, ensuring that data is correctly loaded and split into training and testing sets.

    ***Key Components***
        ***1. DataIngestionConfig***
        @dataclass is a decorator , we dont need to put init again and again for just declaring variables

        A configuration class using the @dataclass decorator to define paths for the training, testing, and raw data files.
        Attributes:
            1) train_data_path: Path to save the training data.
            2) test_data_path: Path to save the testing data.
            3) raw_data_path: Path to save the raw data.

    ***DataIngestion*** 
        A class responsible for the ingestion of data from a source and its preparation for machine learning tasks.

        1) first we are reading data from source it can be any source like Hadoop , database
        
        2) as we make artifact dir so my train,test files will be there and saved there, it use full because if data pipeline crashes we have our data locally available
           another purpose is this data when i train and test split data it will save there cv's in a seperate folder to be used for further procedure 

        3) after spliting saving it to artifact folder

        4) returning data_path of train and test data because it will use in data_transformation class

        5) saving raw data also because if we need to change train , test data then it will work for us
            If the pipeline crashes or needs to be restarted, the raw data is already saved and does not need to be ingested again from the original source.

