# creating an app for my portfolio on streamlit cloud sharing. Using make file to run the app.

#step 1: import libraries
import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from PIL import Image
import os
import time
import datetime

#step 2: create a title and subheader
st.title("Vũ Trọng Ân's Portfolio")
st.subheader("Projects | Machine Learning | Deep Learning | NLP | Data Science | Blogs | Contact")

#step 3: create a sidebar
st.sidebar.title("About me")
st.sidebar.subheader("Vũ Trọng Ân")
st.sidebar.text("Scientist wannabe")
st.sidebar.subheader("Introduction")
st.sidebar.text("Hello! My name is Vũ Trọng Ân. I am an aspiring scientist with a passion for data and technology. I have experience in various data analysis techniques and tools. Through my journey in the world of data, I've been able to provide valuable insights and help make data-driven decisions. This app showcases some of my data visualization projects. Feel free to explore!")

# Load and display the image
image_path = "E:/Work/Coding/portfolio/vutrongan.github.io/materials/image/portrail.jpg"
image = st.sidebar.image(image_path, caption='Vũ Trọng Ân', use_column_width=True)


# Additionally, you can provide links to your social media profiles or your resume:
st.sidebar.subheader("Connect with me")
st.sidebar.markdown("[GitHub](https://github.com/vutrongan)")
st.sidebar.markdown("[Facebook](https://www.facebook.com/vux.aan)")
st.sidebar.markdown("[Zalo]([+84] 093 824 7283)")