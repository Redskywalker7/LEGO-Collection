import pandas as pd

# To DO:

# Create .h file for Functions as a test
# Create conversion table for harry potter subthemes
# Schedule Early morning github update of set and minifig values
# Append Loose minifigures and loose pieces to dataframes
# Instead of scraping each individual Minifigure Page, scrape all minifig values from set page

# App Ideas:
# Metric with delta on it to show how value has exceeded cost
# Checkboxes to select minifigs I want to keep

# Function to generate Brickeconomy URL for set
# Load in datasets

sets = pd.read_csv("Data/sets.csv").rename(columns={'name':'Set Name'})
themes = pd.read_csv("Data/themes.csv").rename(columns={'name':'Theme Name'})
minifigs = pd.read_csv("Data/minifigs.csv")
minifigs_inv = pd.read_csv("Data/inventory_minifigs.csv")
inventories = pd.read_csv("Data/inventories.csv")
inventory_minifigs = pd.read_csv("Data/inventory_minifigs.csv")
Inventory = pd.read_csv("Data/My_Collection.csv")
Wishlist = pd.read_csv("Data/Minifig Wishlist.csv")
Wishlist['Set Number'] = Wishlist['Set Number'].fillna(0).astype(int)

# Join my Inventory to Rebrickable Database
My_sets = Inventory.merge(sets,left_on ='Set Number',right_on = 'set_num',how = 'inner')
My_sets = My_sets.merge(themes,left_on ='Theme_ID',right_on = 'id',how = 'inner')
My_sets = My_sets[['Set Number','Set Name_y','Theme Name','year','num_parts','Acquisition', 'Type',
       'Cost', 'State']].rename(columns={'Set Name_y': 'Set Name','year':'Year','num_parts':'Piece Count', "Theme Name":'Theme'})

# Populate Minifig Database to enable searching inventory by set number
setslist = sets.merge(themes,left_on ='theme_id',right_on = 'id',how = 'inner')
setslist = inventories.merge(setslist,left_on ='set_num',right_on = 'set_num',how = 'inner')
Linked = inventories.merge(setslist,left_on ='set_num',right_on = 'set_num',how = 'inner')
Linked = inventory_minifigs.merge(Linked, left_on = 'inventory_id',right_on = 'id',how = 'inner')
Minifig_Inventory1 = minifigs.merge(Linked, left_on = 'fig_num',right_on = 'fig_num',how = 'inner')
Minifig_Inventory1['Bricklink ID'] = ''

# Join my Inventory to Rebrickable Database to create list of minifigures
the_inventories = My_sets.merge(inventories,left_on ='Set Number',right_on = 'set_num',how = 'inner')
the_inventories = the_inventories[the_inventories.version != 2]
My_Minifigs = inventory_minifigs.merge(the_inventories,left_on ='inventory_id',right_on = 'id',how = 'inner')
My_Minifigs = My_Minifigs.merge(minifigs,left_on ='fig_num',right_on = 'fig_num',how = 'inner')
My_Minifigs = My_Minifigs[['fig_num','name', 'quantity',
       'Theme']].rename(columns={'fig_num':"Rebrickable ID",'name':'Name', 'quantity':'Quantity'})
My_Minifigs['Value'] = 0.0

