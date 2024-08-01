# file name: utils\stacker_3_status.py

import pandas as pd
from utils.database import execute_query
import streamlit as st

@st.cache_data
def get_stacker_3_status():
    """
    Fetch the status of stacker 3 from the database.

    Returns:
        pandas.DataFrame: DataFrame containing the status of stacker 3.
    """
    qry = """
    SELECT Stacker, Cell, Height, Status, Pallet_1, Pallet_2, scrape_date, scrape_time 
    FROM today_cma_status 
    WHERE Stacker = 3
    AND Status NOT IN ('Run', 'Engaged', 'Abort', 'Duplicate')
    ORDER BY Status ASC;
    """

    data = execute_query(qry, fetch=True, db_name='yiduo')
    if data is None:
        raise ConnectionError("Failed to fetch the data from the MySQL database.")
    
    return data
