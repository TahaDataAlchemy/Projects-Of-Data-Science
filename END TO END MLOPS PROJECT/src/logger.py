# This file is made for debugging purpose like 
# 1- if any error occurs it will tell in detail not just print statment: if you upload file and it fails it just not show failed to upload but tell issue like size or format.

# 2- When you use print statements in your code to debug, they only show messages on the console where your program runs. If one class (let's say Class1) has print statements and another class (Class2) calls Class1's methods, the prints from Class1 won't automatically appear in Class2's output unless you specifically print something during that interaction.
    # This means if Class1 encounters an issue or error while Class2 is using it, the print statements in Class1 won't automatically give you detailed information about what went wrong. You might miss crucial details like error messages or where exactly the problem occurred.
    # On the other hand, logging is designed to help in such situations. It lets you record events and errors from different parts of your program systematically. So, if Class1 has logging set up, it can log detailed messages, errors, and even the sequence of events leading to an issue. This makes it easier to trace problems across multiple classes and understand what's happening in your program, especially in more complex scenarios or in production environments.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging Has Started")