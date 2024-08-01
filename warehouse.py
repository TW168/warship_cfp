# file name: warship_cfp/warehouse.py

import pandas as pd
import streamlit as st
import plotly.express as px
from utils.stacker_1_status import get_stacker_1_status
from utils.stacker_2_status import get_stacker_2_status
from utils.stacker_3_status import get_stacker_3_status
from utils.stacker_4_status import get_stacker_4_status
from utils.stacker_5_status import get_stacker_5_status
from utils.database import execute_query

st.title("Warehouse")

# Define a color mapping for the pie charts
color_map = {
    'Couple': '#636EFA',
    '96 inche': '#EF553B',
    'Empty': '#00CC96',
    '48 inch': '#AB63FA',
    'Not Used': '#FFA15A',
    'Disabled': '#19D3F3',
    '9': '#FF6692',
    '12': '#B6E880',
    # Add more statuses and their corresponding colors here
}

# Get the scrape date and time
qry = 'SELECT DISTINCT scrape_date, scrape_time FROM yiduo.today_cma_status;'
scrape_info_df = execute_query(qry, fetch=True, db_name='yiduo')
# Get the first row
first_row = scrape_info_df.iloc[0]
# Extract scrape_date and scrape_time separately
scrape_date = first_row['scrape_date']
scrape_time = first_row['scrape_time']
# If scrape_time is a Timedelta, format it to remove '0 days'
if isinstance(scrape_time, pd.Timedelta):
    scrape_time = str(scrape_time).split(' ')[-1]

contain = st.container()
with contain.expander(f"As of {scrape_date} {scrape_time} Stackers Status", expanded=True):
    df = execute_query('SELECT * FROM v_pancho', fetch=True, db_name='yiduo')
    st.dataframe(df, use_container_width=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Function to create a pie chart with consistent colors and sorted statuses
    def create_pie_chart(data, stacker_title):
        status_counts = data['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        status_counts = status_counts.sort_values(by='Status')  # Sort statuses in ascending order
        fig = px.pie(status_counts, values='Count', names='Status', title=stacker_title, color='Status', color_discrete_map=color_map)
        return fig

    # Stacker 1 Status
    with col1:
        data = get_stacker_1_status()
        fig = create_pie_chart(data, 'Stacker 1')
        st.plotly_chart(fig)
    
    # Stacker 2 Status
    with col2:
        data = get_stacker_2_status()
        fig = create_pie_chart(data, 'Stacker 2')
        st.plotly_chart(fig)
    
    # Stacker 3 Status
    with col3:
        data = get_stacker_3_status()
        fig = create_pie_chart(data, 'Stacker 3')
        st.plotly_chart(fig)
    
    # Stacker 4 Status
    with col4:
        data = get_stacker_4_status()
        fig = create_pie_chart(data, 'Stacker 4')
        st.plotly_chart(fig)
    
    # Stacker 5 Status
    with col5:
        data = get_stacker_5_status()
        fig = create_pie_chart(data, 'Stacker 5')
        st.plotly_chart(fig)
