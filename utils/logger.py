# file name: utils\logger.py

import logging
import os
from config import LOG_DIRECTORY

def setup_logger(function_name):
    """
    Set up a logger for a specific function.

    Args:
        function_name (str): The name of the function for which to set up the logger.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG)
    
    log_file = os.path.join(LOG_DIRECTORY, f'{function_name}.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
    
    return logger
