# file name: app.py

import streamlit as st
from utils.logger import setup_logger

st.set_page_config("CFP Warship", layout="wide", menu_items={"About":""})

logger = setup_logger('app')
warehouse = st.Page("warehouse.py", title="CFP Warship-Warehouse", icon="🏢")
shipping = st.Page("shipping.py", title="CFP Warship-Shipping", icon="📦")
summary = st.Page("summary.py", title="CFP Warship-Summary", icon="📜")
press = st.Page("press.py", title="CFP Warship-Press Release", icon="📰")

# Log page creation
logger.info('Pages created')

pg = st.navigation([warehouse, shipping, summary, press])

# Log navigation setup
logger.info('Navigation setup')

# Run the selected page
try:
    pg.run()
    logger.info('Page run successfully')
except Exception as e:
    logger.error(f'Error running the page: {e}')

