#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
#from datetime import datetime, timedelta, date


def Dollar_Format(x):
  return "${:,.2f}".format(x)

# In[45]:


Sets = pd.read_csv("LEGO Sets.csv")
themes = pd.read_csv("Rebrickable/themes.csv")
main_sets = pd.read_csv("Rebrickable/sets.csv")
my_sets = pd.read_csv("Rebrickable/My_Collection.csv")
my_minifigs = pd.read_csv("Rebrickable/My Minifigs.csv")
minifigs = pd.read_csv("Rebrickable/minifigs.csv")


# In[46]:

Wishlist_Value = Wishlist['Brickeconomy Value'].sum()
Wishlist_Value

Sets.head(5)


# In[47]:

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

Table_Sets.update_layout(margin = dict(l=30,r=10,b=40,t=20))
#Table_Sold.show()

# Pie Chart of New/Sealed Sets
State_Pie = px.pie(Sets, 
                     values='State', 
                     #names=Sources_Count.index,
                     #color_discrete_sequence = colours,
                     labels={'State':'Condition of Set'})
             #hover_data=['lifeExp'], )
State_Pie.update_traces(textposition='inside', textinfo='percent+label')

State_Pie.update_layout(title_text='Set Conditions', title_x=0.488)
#Pie_Sources.show()


# In[49]:


# Streamlit Setup
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
    col1, col2= st.columns([1,1])
    with container2:
        with col1:
            st.metric(label="Value of Wishlist",value=Dollar_Format(Wishlist_Value))
        with col2:
            st.image('logo.png')
            
    st.sidebar.image('Characters/sw0833.jpg', use_column_width=True)
    st.sidebar.image('Minifigs/sw0833.png', use_column_width=True)
    st.plotly_chart(Table_Sets, use_container_width=True)

    
if __name__ == "__main__":
    main()

