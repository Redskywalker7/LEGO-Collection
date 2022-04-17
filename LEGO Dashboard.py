#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import streamlit as st
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta, date


# In[36]:


Sets = pd.read_csv("LEGO Sets.csv")


# In[37]:


Sets.head(5)


# In[38]:


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


# In[43]:


# Streamlit Setup
st.set_page_config(
    #page_title="BPJV SI Database Manager test",
    layout="wide",
    initial_sidebar_state="expanded",
)
def Dollar_Format(x):
  return "${:,.2f}".format(x)

def main():
    st.sidebar.image('Characters/sw0833.jpg', use_column_width=True)
    st.plotly_chart(Table_Sets, use_container_width=True)

    
if __name__ == "__main__":
    main()

