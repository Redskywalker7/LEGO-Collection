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

# FUNCTIONS
def Dollar_Format(x):
  return "${:,.2f}".format(x)

# DATAFRAMES
Sets = pd.read_csv("LEGO Sets.csv")
themes = pd.read_csv("Rebrickable/themes.csv")
main_sets = pd.read_csv("Rebrickable/sets.csv")
my_sets = pd.read_csv("Rebrickable/My_Collection.csv")
my_minifigs = pd.read_csv("Rebrickable/My Minifigs.csv")
minifigs = pd.read_csv("Rebrickable/minifigs.csv")
Wishlist = pd.read_csv("Rebrickable/Minifig Wishlist.csv")

#CALCULATIONS
Wishlist_Value = Wishlist['Brickeconomy Value'].sum()

#TABLES
# Main Set List Table
Table_Sets = go.Figure(data=[go.Table(
    columnwidth = [15,35,25,10,10,15],
    header=dict(values=("<b>Set Number</b>","<b>Set Name</b>","<b>Theme</b>","<b>Type</b>","<b>Acquisition</b>","<b>State</b>"),
                #fill_color=colours[0],
                align='center'),
    cells=dict(values=[Sets['Set Number'],Sets['Set Name'],Sets['Theme'],Sets['Type'],Sets.Acquisition, Sets['State']],
               #fill_color=colours[1],
               align=['center','left','center','center','center','center']))
])
# Wishlist Table
Wishlist_TABLE = go.Figure(data=[go.Table(
    columnwidth = [3,1],
    header=dict(values=("<b>Character</b>","<b>Brickeconomy Value</b>"),
                #fill_color=colours[0],
                align='center'),
    cells=dict(values=[Wishlist['Name'],Wishlist['Brickeconomy Value']],
               #fill_color=colours[1],
               align=['center']))
])

#CHARTS



# STREAMLIT SETUP
st.set_page_config(
    page_title="LEGO Star Wars",
    layout="wide",
    initial_sidebar_state="collapsed",
)
def Dollar_Format(x):
  return "${:,.2f}".format(x)

def main():

    container1 = st.container()
    col1, col2, col3 = st.columns([3,9,1])
    with container1:
        with col1:
            st.image('logo.png')
        with col2:
            st.title("LEGO Star Wars Analysis")
        with col3:
            st.image('Aayla.png')  
    
    container2 = st.container()
    col1, col2, col3= st.columns([1,1])
    with container2:
        with col1:
            st.image("Obi Wan.png")
        with col2:
            st.metric(label="Value of Wishlist",value=Dollar_Format(Wishlist_Value))
        with col3:
            st.plotly_chart(Wishlist_TABLE, use_container_width=True)
            
    st.sidebar.image('Characters/sw0833.jpg', use_column_width=True)
    st.sidebar.image('Minifigs/sw0833.png', use_column_width=True)
    st.plotly_chart(Table_Sets, use_container_width=True)

    
if __name__ == "__main__":
    main()

