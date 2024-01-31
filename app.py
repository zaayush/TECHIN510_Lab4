import time
import streamlit as st

# Define a dictionary of locations and their corresponding time zones
locations = {
    'Seattle': 'US/Pacific',
    'Delhi': 'Asia/Kolkata',
    'Singapore': 'Asia/Singapore',
    # Add more locations as needed
}

# Function to get the current time for a given time zone
def get_current_time(timezone):
    return time.strftime('%d-%b-%Y   %I:%M:%S %p', time.localtime(time.time()))

# Title of the app
st.title('World Clock')

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

# Display the time for each selected location
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
