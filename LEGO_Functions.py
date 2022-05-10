import requests
import time
from bs4 import BeautifulSoup as bs
import LEGO_Datasets as DS

def Generate_link(set_num):
    setslist = sets.merge(themes,left_on ='theme_id',right_on = 'id',how = 'inner')
    if type(set_num) == str:
        url = "https://www.brickeconomy.com/minifig/" + set_num
    else:
        set_num = str(set_num)+"-1"
        theme_ = list(setslist[setslist.set_num == set_num]['Theme Name'])[0].replace(" ","-").lower()
        name_ = list(setslist[setslist.set_num == set_num]['Set Name'])[0].replace(" ","-").lower()
        url = "https://www.brickeconomy.com/set/" + set_num + "/lego-" + theme_ + "-" + name_
    return url 

# Function to determine if set or not and retired or not, then scrape value
def Lego_Value(set_num):
    url = Generate_link(set_num)
    webpage = requests.get(url)
    soup = bs(webpage.content,"html.parser")
    if url[url.find('m/')+2:url.find('m/')+9] == 'minifig':
        Value = soup.find_all("div", {"class": "col-xs-7"})[7].string
    elif soup.find_all("div", {"class": "col-xs-7"})[7].string == "Retired":
        Value = soup.find('b').string
    else:
        Value = soup.find_all("div", {"class": "col-xs-7"})[14].string
    return float(str(Value).replace('$',''))

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
    global set_val     
    for x in range(0,len(set['Rebrickable ID'])):
        if set['Bricklink ID'][x] == '':
            set['Bricklink ID'][x] += Bricklink_ID(set['Rebrickable ID'][x])  
    url = Generate_link(set_num)
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
    if soup.find_all("div", {"class": "col-xs-7"})[7].string == "Retired":
        Value = soup.find('b').string
    else:
        Value = soup.find_all("div", {"class": "col-xs-7"})[14].string
    set_val =  float(str(Value).replace('$',''))
    return set

# Update Values of Current Minifigure Collection
def Update_FigVals():
    for x in range(0,len(My_Minifigs)):
        wait_time = time.time()%10+time.time()%4+1
        fig = (Bricklink_ID(DS.My_Minifigs['Rebrickable ID'][x]))
        DS.My_Minifigs['Value'][x] = Lego_Value(fig)
        time.sleep(wait_time)
