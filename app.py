import time
import streamlit as st

# Define a dictionary of locations and their corresponding time zones
locations = {
    'Seattle': 'US/Pacific',
    'Delhi': 'Asia/Kolkata',
    'Singapore': 'Asia/Singapore',
    # Add more locations as needed
}

# Define a dictionary of locations and their corresponding stock market updates
stock_updates = {
    'Seattle': {
        'NASDAQ': '+0.5%',
        'Apple': '+1.2%',
        'Microsoft': '+0.8%'
    },
    'Delhi': {
        'BSE Sensex': '-1.2%',
        'Tata Motors': '+0.6%',
        'Reliance Industries': '-0.3%'
    },
    'Singapore': {
        'SGX': '+1.8%',
        'DBS Bank': '+0.9%',
        'Singtel': '+1.5%'
    },
    # Add more locations as needed
}

# Function to get the current time for a given time zone
def get_current_time(timezone):
    return time.strftime('%d-%b-%Y   %I:%M:%S %p', time.localtime(time.time()))

# Function to get the stock market update for a given location
def get_stock_update(location):
    return stock_updates.get(location, 'No stock market update available')

# Function to get the top 3 growing stocks for a given location
def get_top_growing_stocks(location):
    stocks = stock_updates.get(location, {})
    sorted_stocks = sorted(stocks.items(), key=lambda x: x[1], reverse=True)
    return sorted_stocks[:3]

# Title of the app
st.title('World Clock and Stock Market Update')

# Allow users to select up to 3 locations
selected_locations = st.multiselect(
    'Select up to 3 locations:',
    list(locations.keys())
)

# Display the time and top 3 growing stocks for each selected location
if selected_locations:
    for location in selected_locations:
        timezone = locations[location]
        current_time = get_current_time(timezone)
        top_growing_stocks = get_top_growing_stocks(location)
        st.write(f'**{location}**')
        st.write(f'Current Time: {current_time}')
        st.write('Top 3 Growing Stocks:')
        for stock, growth in top_growing_stocks:
            st.write(f'{stock}: {growth}')
        st.write('---')



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

    while True:
        for location in selected_locations:
            timezone = locations[location]
            current_time = get_current_time(timezone)
            display_placeholders[location].markdown(
                f'<div style="{circle_style}">{current_time}<br><div style="text-align: center;">{location}</div></div>',
                unsafe_allow_html=True
            )
        time.sleep(1)  # Update every second
