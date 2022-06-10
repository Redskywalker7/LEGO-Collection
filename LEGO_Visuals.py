import pandas as pd
import LEGO_Datasets as LD
import LEGO_Functions as LF
import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go

def tablefunc(table):
    Set_Minifig_Values_Table = go.Figure(data=[go.Table(
    columnwidth = [2,2,5,1,2],
    header=dict(values=("<b>Rebrickable ID</b>","<b>Bricklink ID</b>","<b>Minifig</b>","<b>Quantity</b>","<b>Value</b>"),
                #fill_color=colours[0],
                align='center'),
    cells=dict(values=[table['Rebrickable ID'],table['Bricklink ID'],table['Minifig'],table['Quantity'],table['Value']],
               #fill_color=colours[1],
               align=['left','left','left','center','right']))
    ])
    return Set_Minifig_Values_Table

Wishlist_Table = go.Figure(data=[go.Table(
    columnwidth = [2,5,2,2],
    header=dict(values=("<b>Bricklink ID</b>","<b>Minifigure</b>","<b>Contained Set</b>","<b>Value</b>"),
                #fill_color=colours[0],
                align='center'),
    cells=dict(values=[LD.Wishlist_with_vals['Minifig Number'],LD.Wishlist_with_vals['Name'],LD.Wishlist_with_vals['Set Number'],LD.Wishlist_with_vals['Minifig Value']],
               #fill_color=colours[1],
               align=['left','left','center','center']))
    ])
Wishlist_Table.update_layout(margin=dict(l=5,r=5,b=10,t=10))
