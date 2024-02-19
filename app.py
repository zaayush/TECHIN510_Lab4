
import time
import streamlit as st
import yfinance as yf
from datetime import datetime
import pytz
# Define a dictionary of locations and their corresponding time zones
locations = {
    'Seattle': 'US/Pacific',
    'Delhi': 'Asia/Kolkata',
    'Singapore': 'Asia/Singapore',
    # Add more locations as needed
}


# Function to get the current time for a given time zone
def get_current_time(tzone):
    zone = pytz.timezone(tzone) 
    timeinzone = datetime.now(zone)
    currentTime = timeinzone.strftime("%d-%b-%Y   %I:%M:%S %p")
    return currentTime

def pick_stock_symbol(location):
    if location == 'Seattle':
        stock_name = 'Amazon'
        stock_symbol = 'AMZN'
        
    elif location == 'Delhi':
        stock_name = 'Reliance Industries'
        stock_symbol = 'RELIANCE.NS'
        
    elif location == 'Singapore':
        stock_name = 'DBS Group Holdings'
        stock_symbol = 'D05.SI'
    else:
        return None
    return stock_symbol, stock_name 


def display_stock_data(stock_symbol, stock_name):
    stock = yf.Ticker(stock_symbol)
    st.subheader(f"Stock: {stock_name}")
    stock_data = stock.history(period="360d")
    st.line_chart(stock_data["Close"])
    stock_data2 = stock.history(period="3d")
    stock_data2 = stock_data2.drop(columns=['Dividends', 'Stock Splits'])
    st.write(stock_data2)

# Title of the app
st.title('World Clock and Stock Market Update')

# Allow users to select up to 3 locations
selected_locations = st.multiselect(
    'Select up to 3 locations:',
    list(locations.keys())
)


# Define CSS style for the circular display
circle_style = '''
    border-radius: 50%;
    background-color: #262730;
    width: 500px;
    height: 500px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 2em;
    margin: 20px;
'''

# Display the time for each selected location in a circular display
if selected_locations:
    display_placeholders = {}
    for location in selected_locations:
        display_placeholders[location] = st.empty()
        # Display stock data for each selected location
        stock_symbol, stock_name = pick_stock_symbol(location)  
        display_stock_data(stock_symbol, stock_name)
    while True:
        for location in selected_locations:
            tzone = locations[location]
            current_time = get_current_time(tzone)
            display_placeholders[location].markdown(
                f'<div style="{circle_style}">{current_time}<br><div style="text-align: center;">{location}</div></div>',
                unsafe_allow_html=True
            )
            
        time.sleep(1)  # Update every second
