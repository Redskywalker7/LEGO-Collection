#!/usr/bin/env python
# coding: utf-8

import LEGO_Functions as LF
import LEGO_Visuals as LV
import streamlit as st

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
            
choice = st.text_input(label = "Enter set or minifigure number",placeholder = "75020")

if LF.testvar(choice) == True:
    st.plotly_chart(LV.tablefunc(choice),use_container_width=True)
  
if __name__ == "__main__":
    main()



