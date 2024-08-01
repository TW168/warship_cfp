import mysql.connector
from mysql.connector import Error
import pandas as pd
from .logger import setup_logger
from config import get_database_config

def create_connection(db_name='yiduo'):
    """
    Establish a connection to the MySQL database.

    Args:
        db_name (str): The name of the database configuration to use.

    Returns:
        connection (mysql.connector.connection.MySQLConnection): The MySQL connection object if connected successfully, else None.
    """
    logger = setup_logger('create_connection')
    db_config = get_database_config(db_name)
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        if connection.is_connected():
            logger.info('Successfully connected to the database')
            return connection
    except Error as e:
        logger.error(f'Error while connecting to MySQL: {e}')
        return None

def execute_query(query, params=None, fetch=False, db_name='yiduo'):
    """
    Execute a SQL query on the MySQL database.

    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters to pass with the SQL query.
        fetch (bool, optional): Whether to fetch the results as a pandas DataFrame.
        db_name (str): The name of the database configuration to use.

    Returns:
        pandas.DataFrame or None: DataFrame containing the query results if fetch is True, else None.
    """
    logger = setup_logger('execute_query')
    connection = create_connection(db_name)
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if fetch:
                result = cursor.fetchall()
                df = pd.DataFrame(result)
                logger.info(f'Query executed and data fetched: {query}')
                return df
            else:
                connection.commit()
                logger.info(f'Query executed successfully: {query}')
        except Error as e:
            logger.error(f'Error executing query: {e}')
        finally:
            cursor.close()
            connection.close()
    return None
