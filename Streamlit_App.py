#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import LEGO_Datasets as LD
import LEGO_Functions as LF
import LEGO_Visuals as LV
import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# FUNCTIONS
def Dollar_Format(x):
  return "${:,.2f}".format(x)
colours = ( "cadetblue", "turquoise", "skyblue",
          "lightsteelblue","azure","teal")

# STREAMLIT SETUP
st.set_page_config(
    page_title="LEGO Collection Analysis",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def main():
    container1 = st.container()
    col1, col2 = st.columns([5,5])
    with container1:
        with col1:
            st.image('Pictures/sw0833.png')
        with col2:
            st.image('Pictures/Aayla.jpg')  
            
input = st.text_input(label = "Enter set or minifigure number")
st.plotly_chart(LV.Set_Minifig_Values_Table,use_container_width=True)
  
if __name__ == "__main__":
    main()

str("Hello there")
