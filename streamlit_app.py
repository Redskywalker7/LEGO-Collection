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
colours = ( "cadetblue", "turquoise", "skyblue",
          "lightsteelblue","azure","teal")
#def FilterMovie(option):
   

# DATAFRAMES
Sets = pd.read_csv("LEGO Sets.csv")
themes = pd.read_csv("Rebrickable/themes.csv")
main_sets = pd.read_csv("Rebrickable/sets.csv")
my_sets = pd.read_csv("Rebrickable/My_Collection.csv")
my_minifigs = pd.read_csv("Rebrickable/My Minifigs.csv")
minifigs = pd.read_csv("Rebrickable/minifigs.csv")
Wishlist = pd.read_csv("Rebrickable/Minifig Wishlist.csv")
Star_Wars = Sets[Sets.Theme == 'Star Wars']
SW_Minifigs = my_minifigs[my_minifigs.Theme == 'Star Wars']


#CALCULATIONS
Wishlist_Value = Wishlist['Brickeconomy Value'].sum()
Movies = pd.DataFrame(my_minifigs['SubTheme'].value_counts())
Wish_Count = len(Wishlist)

#TABLES
# Main Set List Table
Table_Sets = go.Figure(data=[go.Table(
    columnwidth = [15,35,25,10,10,15],
    header=dict(values=("<b>Set Number</b>","<b>Set Name</b>","<b>Theme</b>","<b>Type</b>","<b>Acquisition</b>","<b>State</b>"),
                #fill_color=colours[0],
                align='center'),
    cells=dict(values=[Star_Wars['Set Number'],Star_Wars['Set Name'],Star_Wars['Theme'],Star_Wars['Type'],Star_Wars.Acquisition, Star_Wars['State']],
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
Wishlist_TABLE.update_layout(
    title_text="LEGO Star Wars Minifigure Wishlist",
    title_x=0.5
)

#CHARTS
Movies_CHART = px.pie(Movies, 
                     values=Movies['SubTheme'], 
                     names=Movies.index,
                     color_discrete_sequence = colours,
                     labels={'SubTheme':'Movies'})
             #hover_data=['lifeExp'], )
Movies_CHART.update_traces(textposition='inside', textinfo='percent+label')

Movies_CHART.update_layout(title_text='Minifigure Collection by Movie', title_x=0.488)
#Pie_Sources.show()


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
    col1, col2, col3 = st.columns([5,15,2])
    with container1:
        with col1:
            st.image('Pictures/logo.png')
        with col2:
            st.title("LEGO Star Wars Minifigure Analysis")
        with col3:
            st.image('Pictures/Aayla.png')  
    
    container2 = st.container()
    col1, col2, col3 = st.columns([1,1,1])
    with container2:
        with col1:
            st.metric(label="Collection Count",value=len(my_minifigs))
        with col2:
            st.metric(label="Value of Wishlist",value=Dollar_Format(Wishlist_Value))
        with col3:
            st.metric(label="Wishlist Count",value=Wish_Count)
        
    
    container3 = st.container()
    col1, col2, col3= st.columns([1,2,2])
    with container3:
        with col1:
            st.image("Pictures/Obiwan.png",width = 200)
        with col2:
            st.plotly_chart(Movies_CHART, use_container_width=True)
        with col3:
            st.plotly_chart(Wishlist_TABLE, use_container_width=True)
    st.sidebar.header("TEST")        
    st.sidebar.image('Characters/sw0833.jpg', use_column_width=True)
    
    container4 = st.container()
    col1, col2 = st.columns([1,2])
    with container4:
        with col1:
            option = st.selectbox("Select Movie",['All Movies'] + Movies.index.tolist())
            if(option != 'All Movies'):
                Filtered = SW_Minifigs[SW_Minifigs['SubTheme'] == option]
                SW_Minifigs_TABLE = go.Figure(data=[go.Table(
                    columnwidth = [1,3,2],
                    header=dict(values=("<b>Set Number</b>","<b>Character</b>","<b>Movie</b>"),
                                align='center'),
                    cells=dict(values=[Filtered['Set Number'],Filtered['Name'],Filtered['SubTheme']],
                               align='center')
                )])
                SW_Minifigs_TABLE.update_layout(
                    title_text="Current LEGO Star Wars Minifigure Collection",
                    title_x=0.5
                )
            else:
                SW_Minifigs_TABLE = go.Figure(data=[go.Table(
                    columnwidth = [1,3,2],
                    header=dict(values=("<b>Set Number</b>","<b>Character</b>","<b>Movie</b>"),
                                align='center'),
                    cells=dict(values=[SW_Minifigs['Set Number'],SW_Minifigs['Name'],SW_Minifigs['SubTheme']],
                               align='center')
                )])
                SW_Minifigs_TABLE.update_layout(
                    title_text="Current LEGO Star Wars Minifigure Collection",
                    title_x=0.5
                )
        with col2:
            st.plotly_chart(SW_Minifigs_TABLE, use_container_width=True)

    
if __name__ == "__main__":
    main()

