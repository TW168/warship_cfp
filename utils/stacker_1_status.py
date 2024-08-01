# file name: utils\stacker_1_status.py

import pandas as pd
from utils.database import execute_query
from utils.logger import setup_logger
import streamlit as st

@st.cache_data
def get_stacker_1_status():
    """
    Fetch the status of stacker 1 from the database.

    Returns:
        pandas.DataFrame: DataFrame containing the status of stacker 1.
    """
    logger = setup_logger('get_stacker_1_status')
    qry = """
    SELECT Stacker, Cell, Height, Status, Pallet_1, Pallet_2, scrape_date, scrape_time 
    FROM today_cma_status 
    WHERE Stacker = 1
    AND Status NOT IN ('Run', 'Engaged', 'Abort', 'Duplicate')
    ORDER BY Status ASC;
    """
    logger.info('Executing query to fetch stacker 1 status')

    try:
        data = execute_query(qry, fetch=True, db_name='yiduo')
        if data is None:
            logger.error('Failed to fetch the data from the MySQL database')
            raise ConnectionError("Failed to fetch the data from the MySQL database.")
        logger.info('Successfully fetched stacker 1 status')
    except Exception as e:
        logger.error(f'Error fetching stacker 1 status: {e}')
        raise
    
    return data
