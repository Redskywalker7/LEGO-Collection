import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# Load in datasets
sets = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\sets.csv").rename(columns={'name':'Set Name'})
themes = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\themes.csv").rename(columns={'name':'Theme Name'})
minifigs = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\minifigs.csv")
minifigs_inv = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\inventory_minifigs.csv")
inventories = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\inventories.csv")
inventory_minifigs = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\inventory_minifigs.csv")
Inventory = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\My_Collection.csv")

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

# Test sets or Minifigs
Pod = 'https://www.brickeconomy.com/set/75258-1/lego-star-wars-anakins-podracer-20th-anniversary-edition'
Falcon = 'https://www.brickeconomy.com/set/75192-1/lego-star-wars-millennium-falcon'
Looney = 'https://www.brickeconomy.com/set/71030-3/lego-minifigure-series-looney-tunes-wile-e-coyote'
Queen = 'https://www.brickeconomy.com/minifig/sw0387/queen-amidala'

# Determine if set or not and retired or not, then scrape value
webpage = requests.get(Queen)
soup = bs(webpage.content,"html.parser")
if soup.find_all("div", {"class": "col-xs-7"})[7].string == "Retired":
    Value = soup.find('b').string
elif soup.find_all('h4')[8].string == 'Minifig Details':
    Value = soup.find('b').string
else:
    Value = soup.find_all("div", {"class": "col-xs-7"})[14].string
Value

