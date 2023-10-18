# creating an portfolio app using streamlit
# step 1:
# import the libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

# step 2:
# create a title for the app
st.title("Portfolio App")

# step 3:
# create a sidebar for the app to add the widgets
st.sidebar.title("Portfolio App")
st.sidebar.subheader("Data Visualization")
st.sidebar.subheader("About App")

# step 4:
# load the data
df = pd.read_csv("https://raw.githubusercontent.com/ThuwarakeshM/PracticalML-KMeans-Election/master/voters_demo_sample.csv")
df

# step 5:
# add widgets to the sidebar for data visualization and add a checkbox to show the data
if st.sidebar.checkbox("Show Data", False):
    st.write(df)

# add a checkbox to the sidebar
if st.sidebar.checkbox("Show Columns"):
    all_columns = df.columns.to_list()
    st.write(all_columns)

# add a checkbox to the sidebar
if st.sidebar.checkbox("Summary"):
    st.write(df.describe())

# add a checkbox to the sidebar
if st.sidebar.checkbox("Show Selected Columns"):
    selected_columns = st.multiselect("Select Columns", all_columns)
    new_df = df[selected_columns]
    st.dataframe(new_df)

# add a checkbox to the sidebar
if st.sidebar.checkbox("Show Value Counts"):
    st.write(df.iloc[:,-1].value_counts())

# add a checkbox to the sidebar
if st.sidebar.checkbox("Correlation with Seaborn"):
    st.write(sns.heatmap(df.corr(), annot=True))
    st.pyplot()