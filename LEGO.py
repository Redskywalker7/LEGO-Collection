import pandas as pd
from pyparsing import lineEnd
import requests
from bs4 import BeautifulSoup as bs

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
def set_link(set_num):
    set_num = str(set_num)+"-1"
    setslist = sets.merge(themes,left_on ='theme_id',right_on = 'id',how = 'inner')
    theme_ = list(setslist[setslist.set_num == set_num]['Theme Name'])[0].replace(" ","-").lower()
    name_ = list(setslist[setslist.set_num == set_num]['Set Name'])[0].replace(" ","-").lower()
    url = "https://www.brickeconomy.com/set/" + set_num + "/lego-" + theme_ + "-" + name_
    return url 

# Function to determine if set or not and retired or not, then scrape value
def Lego_Value(url):
    webpage = requests.get(url)
    soup = bs(webpage.content,"html.parser")
    if url[url.find('m/')+2:url.find('m/')+9] == 'minifig':
        Value = soup.find_all("div", {"class": "col-xs-7"})[7].string
    elif soup.find_all("div", {"class": "col-xs-7"})[7].string == "Retired":
        Value = soup.find('b').string
    else:
        Value = soup.find_all("div", {"class": "col-xs-7"})[14].string
    return Value

# Function to get Bricklink ID from Rebrickable link
def Bricklink_ID(Fig):
    url = 'https://rebrickable.com/minifigs/'+Fig
    webpage = requests.get(url)
    soup = bs(webpage.content,"html.parser")
    link = str(soup.find_all('td')[15:])
    link = link[link.find('q=')+2:link.find('&')]
    return link
    
# Function to return Minifigure Inventory from Set Number
def Minifigs_Search(set_num):
    set_num = str(set_num)+"-1"
    Minifig_Inventory = Minifig_Inventory1[Minifig_Inventory1['set_num'] == set_num]
    Minifig_Inventory = Minifig_Inventory[Minifig_Inventory.version_y == 1]
    Minifig_Inventory = Minifig_Inventory[Minifig_Inventory.version_x == 1]
    Minifigures =  Minifig_Inventory[['fig_num','Bricklink ID','name','quantity']].rename(columns={'fig_num': 'Rebrickable ID','name':'Minifig','quantity':'Quantity'})
    Minifigures['Value'] = 0.0
    return Minifigures

# Function to find the value of all the minifigures in a set
def Set_Minifig_Values(set_num):
    set = Minifigs_Search(set_num)    
    set = set.reset_index()    
    for x in range(0,len(set['Rebrickable ID'])):
        if set['Bricklink ID'][x] == '':
            set['Bricklink ID'][x] += Bricklink_ID(set['Rebrickable ID'][x])  
    url = set_link(set_num)
    webpage = requests.get(url)
    soup = bs(webpage.content,"html.parser")
    list_items = soup.find_all("div", {"class": "setminifigpanel-number"})   
    for x in range(0,len(list_items)):
        string = str(soup.find_all("div", {"class": "setminifigpanel-number"})[x])
        fig_num = string[string.find("<span>")+6:string.find("</s")]
        val_link = soup.find_all("div", {"class": "setminifigpanel-value"})[x]
        fig_val = float(str(val_link)[int(str(val_link).find("$"))+1:int(str(val_link).find("</div>"))])
        if fig_num in list(set['Bricklink ID']):
            indx = list(set['Bricklink ID']).index(fig_num) # Problem here. ValueError: None is not in list
            set['Value'][indx] = fig_val
    return set


# Load in datasets
sets = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\sets.csv").rename(columns={'name':'Set Name'})
themes = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\themes.csv").rename(columns={'name':'Theme Name'})
minifigs = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\minifigs.csv")
minifigs_inv = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\inventory_minifigs.csv")
inventories = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\inventories.csv")
inventory_minifigs = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\inventory_minifigs.csv")
Inventory = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\My_Collection.csv")
Wishlist = pd.read_csv(r"C:\Users\lukejo\Documents\Data\Practice\Minifig Wishlist.csv")

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

# Loop to populate My_Minifigs with brickeconomy values 
#for x in range(0,len(My_Minifigs)-1):
#    fig = (My_Minifigs['Rebrickable ID'][x])
#    My_Minifigs['Value'][x] = float(Lego_Value('https://www.brickeconomy.com/minifig/'+Bricklink_ID(fig)).replace('$',''))


# Tests
Lego_Value('https://www.brickeconomy.com/minifig/sw0485')
Lego_Value('https://www.brickeconomy.com/set/75020-1/lego-star-wars-jabbas-sail-barge')

set_link(9516)
Set_Minifig_Values(75020)

Minifigs_Search(75020)
Minifigs_Search(9499)
