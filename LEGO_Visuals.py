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

Wishlist_Table = Set_Minifig_Values_Table = go.Figure(data=[go.Table(
    columnwidth = [2,2,5,1,2,1,1],
    header=dict(values=("<b>Bricklink ID</b>","<b>Rebrickable ID</b>","<b>Minifigure</b>","<b>Theme</b>","<b>Contained Set</b>","<b>Value</b>"),
                #fill_color=colours[0],
                align='center'),
    cells=dict(values=[LD.Wishlist_with_vals['Minifig Number'],LD.Wishlist_with_vals['Rebrickable ID'],LD.Wishlist_with_vals['Name'],LD.Wishlist_with_vals['Theme'],LD.Wishlist_with_vals['Set Number'],,LD.Wishlist['Value']],
               #fill_color=colours[1],
               align=['left','left','left','center','right','center']))
    ])
