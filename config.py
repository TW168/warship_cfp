# file name: config.py

import configparser
import os

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

def get_database_config(db_name='yiduo'):
    """
    Get the database configuration for the specified database.

    Args:
        db_name (str): The name of the database section in the config file.

    Returns:
        dict: Database configuration parameters.
    """
    db_config = {
        'host': config[db_name]['host'],
        'user': config[db_name]['user'],
        'password': config[db_name]['password'],
        'database': config[db_name]['database']
    }
    return db_config

# Log file configuration
LOG_DIRECTORY = config['logging']['log_directory']

# Ensure log directory exists
os.makedirs(LOG_DIRECTORY, exist_ok=True)
