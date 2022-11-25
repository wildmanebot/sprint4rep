
#read in required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

#read in CSV file
vehicles_df = pd.read_csv('vehicles_us.csv')

#header text
st.header('A Closer Look at Drivetrain Types in the Used Vehicle Market')

#Description of the purpose of the page
st.write('We will take a closer look at the differences between 4wd and 2wd drivetrain type vehicles.') 

#create df with average price vs condition of vehicles data
pc_df = vehicles_df.groupby('condition')['price'].mean().round(0).astype('int')

#plotly chart settings
fig = px.bar(pc_df, y="price",
title="Average Price of Vehicle listings versus their Condition", color="price",
labels={"price": "Average Price ($)", "condition": "Condition"})
fig.update_xaxes(categoryorder='array', categoryarray= ['new', 'like new', 'excellent', 'good', 'fair', 'salvage'])
fig.update(layout_coloraxis_showscale=False)

# showing the barchart of average price vs condition
st.plotly_chart(fig, use_container_width=True)

#create checkboxes
cbox_4wd = st.checkbox('Display 4wd Vehicles')

if cbox_4wd:
    st.write('test')


