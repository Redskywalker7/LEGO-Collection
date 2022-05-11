#!/usr/bin/env python
# coding: utf-8

#LIBRARIES
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
#from datetime import datetime, timedelta, date


# STREAMLIT SETUP
st.set_page_config(
    page_title="LEGO Star Wars",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def main():
    container1 = st.container()
    col1, col2 = st.columns([5,15])
    with container1:
        with col1:
            st.image('Pictures/sw0833.png')
        with col2:
            st.image('Pictures/Aayla.jpg')  
  
if __name__ == "__main__":
    main()

