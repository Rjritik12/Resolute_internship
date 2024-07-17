import pandas as pd
import streamlit as st  # type: ignore

# Load the raw data
df = pd.read_csv('rawdata.xlsx - inputsheet.csv')

# Convert the 'date' and 'time' columns to datetime format
# Combine date and time columns and specify the format
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%m/%d/%Y %I:%M:%S %p') 

# Calculate the datewise total duration for each inside and outside
df_inside = df[df['location'] == 'inside']
df_outside = df[df['location'] == 'outside']

inside_duration = df_inside.groupby(df_inside['datetime'].dt.date)['number'].sum()
outside_duration = df_outside.groupby(df_outside['datetime'].dt.date)['number'].sum()

# Calculate the datewise number of picking and placing activity done
picking_activity = df[df['activity'] == 'picking'].groupby(df['datetime'].dt.date)['activity'].count()
placing_activity = df[df['activity'] == 'placing'].groupby(df['datetime'].dt.date)['activity'].count()

# Create a Streamlit app
st.title("Raw Data Analysis")

# Display the datewise total duration for each inside and outside
st.header("Datewise Total Duration")
st.write("Inside:")
st.write(inside_duration)
st.write("Outside:")
st.write(outside_duration)

# Display the datewise number of picking and placing activity done
st.header("Datewise Number of Picking and Placing Activity")
st.write("Picking:")
st.write(picking_activity)
st.write("Placing:")
st.write(placing_activity)

# Run the Streamlit app

