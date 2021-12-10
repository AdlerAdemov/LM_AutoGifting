#
#   LordsMobile AutoGifting with code (by Addo)
#
#######  IMPORTING THE LIBRARIES #######
from urllib.request import urlopen
import requests
import time
import pandas as pd #"Pandas" tool to parse the excel (.xlsx) file, generated from the Bot
from collections import OrderedDict #For removing duplicates

# REMEMBER TO CHANGE THE NAME OF THE NEWLY GENERATED EXCEL FILE FROM THE Lords-Bot!
excel_file = pd.read_excel('2021-29-11 13-37 OnE.xlsx', usecols = 'B')
excel_file.head()
df = pd.DataFrame(excel_file)

#Converting Pandas DataFrame into a List
gnames = df['Name'].values.tolist()

#Accounts that should be gifted, nomather which guild is being put
myaccounts = ['ADLER', 'AddoX', 'BoredOwl', 'Warzone911', 'Add Food', 'Add Wood', 'Add Stone', 'Add Ore', 'Sizzor', 'Bad Juju 4 U', 'Sloppysecnds', 'Sick Titties', 'Bad Bltch', 'Royal FuQuad', 'Royal Douche', 'Stoney Banks', 'Mine Fieldz', 'ItsJujuBltch', 'HerbalHoebag', 'FoodProHoe01', 'FoodProHoe2', 'Monkey Butt']
gnames.extend(myaccounts)

#Keeping the right order
ordered_gnames = list(OrderedDict.fromkeys(gnames))

#Converting list to tuple
all_names_as_list = tuple(ordered_gnames)

#Listing all players that will be gifted
print(all_names_as_list)
print("Total players: ",len(all_names_as_list))

######################################################################################################################

#Asking the user to enter the gift code
giftcode = input("Please insert the GiftCode: ")

#Going through the whole list of players and submitting their names with the given gift code
for player in all_names_as_list:
    print(player)
    time.sleep(1.5)
    
    #Checking if the player exists
    playerCheck = requests.post('https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902', data={'ac':'get_extra_info', 'charname': player, 'lang': 'en'})
    print(playerCheck.text)

    #Submitting the gift code
    submitting = requests.post('https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902', data={'ac':'get_gifts', 'type':'1', 'iggid':'0', 'charname': player, 'cdkey': giftcode, 'lang': 'en'})
    print(submitting.text)