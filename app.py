
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

#Fills missing values in is_4wd column with string '2wd' (two wheel drive) and converts entire column to string (object Dtype)
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna('2wd').astype('str')

#Replaces values of 1 (with the assumption that a value of 1 means that vehicle is 4wd) with string '4wd'
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].replace(['1.0'], '4wd')

#Renames is_4wd column to something more intuitive - "drivetrain"
vehicles_df = vehicles_df.rename(columns={'is_4wd': 'drivetrain'})

vehicles_df = vehicles_df.loc[vehicles_df['model_year'] > 1975]
vehicles_df = vehicles_df.loc[vehicles_df['price'] <= 100000]
pc_df = vehicles_df
fig = px.scatter(pc_df, x="price", y="model_year", color="drivetrain")
fig.update_layout(xaxis_title="Price", yaxis_title="Model Year")
st.plotly_chart(fig, use_container_width=True)

#create checkboxes
cbox_4wd = st.checkbox('Display 4wd Vehicles', value=True)
cbox_2wd = st.checkbox('Display 2wd vehicles', value=True)

if cbox_4wd and cbox_2wd:
    pc_df = vehicles_df
elif cbox_4wd and not cbox_2wd:
    pc_df = vehicles_df.loc[vehicles_df['drivetrain'] == '4wd']  
elif not cbox_4wd and cbox_2wd:
    pc_df = vehicles_df.loc[vehicles_df['drivetrain'] == '2wd']   
elif not cbox_4wd and not cbox_2wd:
    pc_df = vehicles_df
    
fig = px.histogram(pc_df, title='Number of Vehicles with Specific Drivetrain vs. Price', x='price', color='drivetrain', nbins=50, barmode='overlay')
fig.update_layout(xaxis_title="Price", yaxis_title="Number of Vehicles", yaxis_range=[0,5000])
# showing the histogram of drivetrain vs price
st.plotly_chart(fig, use_container_width=True)






