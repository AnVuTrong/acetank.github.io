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

# STYLE:
'''
lighter
----------------
nyanza = '#E5F9E0'
light_green = '#A3F7B5'
viridian = '#57886C'
feldgrau = '#466060'
rich_black = '#0E0F19'
----------------
darker
'''

# Create a title and subheader
st.title("ACEtankACE's Portfolio")
st.caption("WELCOME TO MY PERSONAL PORTFOLIO - Vũ Trọng Ân")

# Menu options
# Define the sections and their corresponding background colors
pages = {
    "🚀 Projects": "#E5F9E0",
    "🤖 Machine Learning": "#E5F9E0",
    "🧠 Deep Learning": "#E5F9E0",
    "🗣️ NLP": "#E5F9E0", 
    "📊 Data Science": "#E5F9E0",
    "📝 Blogs": "#E5F9E0",
    "📞 Contact": "#E5F9E0"
}

# Button style
st.markdown("""
    <style>
        .btn-style {
            display: inline-block;
            padding: 0.5em 1.5em;
            font-size: 16px;
            border: none;
            color: #E5F9E0;
            background-color: #0E0F19;
            text-align: left;
            cursor: pointer;
            outline: none;
            width: 100%;
            border-radius: 10px;
            margin: 0.5em 0;
            transition: background-color 0.3s, color 0.3s;
        }
        
        .btn-style:hover {
            background-color: #E5F9E0;
            color: #0E0F19;
        }
    </style>
""", unsafe_allow_html=True)

selected_page = None
for page, color in pages.items():
    if st.sidebar.markdown(f'<button class="btn-style" style="background-color: {color}">{page}</button>', unsafe_allow_html=True):
        selected_page = page

# click on the button to select a page
if selected_page:
    st.title(selected_page)
    if selected_page == "🚀 Projects":
        st.write("Projects content goes here!")


# Contact section
st.sidebar.subheader("Connect with me")
st.sidebar.markdown("[GitHub](https://github.com/vutrongan)")
st.sidebar.markdown("[Facebook](https://www.facebook.com/vux.aan)")
st.sidebar.markdown("[Zalo]([+84] 093 824 7283)")