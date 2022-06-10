#!/usr/bin/env python
# coding: utf-8

import LEGO_Functions as LF
import LEGO_Datasets as LD
import LEGO_Visuals as LV
import streamlit as st

# STREAMLIT SETUP
st.set_page_config(
    page_title="LEGO Collection Analysis",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def main():
#    container1 = st.container()
#    col1, col2 = st.columns([5,5])
#    with container1:
#        with col1:
#            st.image('Pictures/sw0833.png')
#
#        with col2:
#            st.image('Pictures/Aayla.jpg')  
    #st.metric(label = "What are we getting here", value = choice)
    #st.plotly_chart(LV.tablefunc(choice),use_container_width=True) 
    choice = ''
    choice = st.text_input(label = "Enter set or minifigure ID",placeholder = '75020')
    #st.metric(label = "Set Value", value = LF.set_val)
    if len(choice) > 0:
        table = LF.Set_Minifig_Values(choice)
        set_table = LV.tablefunc(table)
        Minifig_Values = (table.Quantity*table.Value).sum()
        Set_Name = list(LD.setslist[LD.setslist['set_num'] == (str(choice)+"-1")]['Set Name'])[0]
        container1 = st.container()
        col1, col2, col3, col4  = st.columns([8,4,4,4])
        with container1:
            with col1:
                st.metric(label = "Set Name", value = Set_Name)
            with col2:
                st.metric(label = "Set Value", value = LF.Dollar_Format(LF.set_val))
            with col3:
                st.metric(label = "Total Minifigs Value", value = LF.Dollar_Format(Minifig_Values))
            with col4:
                st.metric(label = "Set Value w/o Minifigs", value = LF.Dollar_Format(LF.set_val - Minifig_Values))             
        st.plotly_chart(set_table,use_container_width=True) 
    container2 = st.container()
    col5, col6, col7  = st.columns([1,1,1])
    with container2:
        with col5:
            st.metric(label = "Total Value of Wishlist", value = LF.Dollar_Format(sum(DS.Wishlist_with_vals['Minifig Value'])))
        with col6:
            st.metric(label = "Wishlist Minifigs", value = len(DS.Wishlist_with_vals['Minifig Value']))   
        with col7:
            st.metric(label = "Unique Sets", value = len(DS.Wishlist['Set Number'].value_counts()))          
    st.plotly_chart(LV.Wishlist_Table,use_container_width=True)  

if __name__ == "__main__":
    main()
