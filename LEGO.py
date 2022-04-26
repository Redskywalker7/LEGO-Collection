import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# Load in datasets
sets = pd.read_csv("Rebrickable\sets.csv").rename(columns={'name':'Set Name'})
themes = pd.read_csv("Rebrickable\themes.csv").rename(columns={'name':'Theme Name'})
minifigs = pd.read_csv("Rebrickable\minifigs.csv")
minifigs_inv = pd.read_csv("Rebrickable\inventory_minifigs.csv")
inventories = pd.read_csv("Rebrickable\inventories.csv")
inventory_minifigs = pd.read_csv("Rebrickable\inventory_minifigs.csv")
Inventory = pd.read_csv("Rebrickable\My_Collection.csv")

# Join my Inventory to Rebrickable Database
My_sets = Inventory.merge(sets,left_on ='Set Number',right_on = 'set_num',how = 'inner')
My_sets = My_sets.merge(themes,left_on ='Theme_ID',right_on = 'id',how = 'inner')
My_sets = My_sets[['Set Number','Set Name_y','Theme','year','num_parts','Acquisition', 'Type',
       'Cost', 'State']].rename(columns={'Set Name_y': 'Set Name','year':'Year','num_parts':'Piece Count'})

# Join my Inventory to Rebrickable Database to create list of minifigures
the_inventories = My_sets.merge(inventories,left_on ='Set Number',right_on = 'set_num',how = 'inner')
the_inventories = the_inventories[the_inventories.version != 2]
My_Minifigs = inventory_minifigs.merge(the_inventories,left_on ='inventory_id',right_on = 'id',how = 'inner')
My_Minifigs = My_Minifigs.merge(minifigs,left_on ='fig_num',right_on = 'fig_num',how = 'inner')
My_Minifigs = My_Minifigs[['fig_num','name', 'quantity',
       'Theme']].rename(columns={'fig_num':"Rebrickable ID",'name':'Name', 'quantity':'Quantity'})
