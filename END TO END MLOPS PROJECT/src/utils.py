# Utility Functions: Often, a utils file contains various utility functions that are used across different parts of your application. These functions are typically small, reusable pieces of code that perform common tasks or operations. By centralizing these functions in one file (or module), you avoid duplicating code throughout your project.

# Code Organization: Grouping utility functions into a single file helps organize your codebase. Instead of scattering similar functions across multiple files, you can locate them easily in one place. This improves code maintainability and readability, as developers can quickly find and understand the purpose of each utility function.

import os
import dill # use for creating pickle file (pkl)
import numpy as np
import sys
import pandas as pd
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.append(project_root)
from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)