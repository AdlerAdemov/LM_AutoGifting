#
#   LordsMobile AutoGifting with code
#
#######  IMPORTING THE LIBRARIES #######
from lxml.cssselect import CSSSelector
from urllib.request import urlopen
import lxml.html
import requests
import time
import sys

###############################################################################################################################################
################################## THE CSS SELECTOR WAY OF PARSING THE GUILD NAMES (without kingdoms) #########################################
print("======================================================================================================================================")
print("THE CSS SELECTOR WAY OF PARSING THE GUILD NAMES (without kingdoms)")
#Parsing the guild page

# To gift to OnE, uncomment this
url =  "https://lordsmobilemaps.com/en/alliance/OnE%20UNITED"

# To gift to DI2, uncomment this
#url =  "https://lordsmobilemaps.com/en/alliance/District12"

# To gift to d|E, uncomment this
#url =  "https://lordsmobilemaps.com/en/alliance/The%20Devils%20Elite"

response = requests.get(url, stream=True)
response.raw.decode_content = True
tree = lxml.html.parse(response.raw)

#(Method 1) Taking the names of the players with lxml's CSS Selector module
guild_players = CSSSelector('.tobtab2col div:nth-of-type(n+2) div:nth-of-type(2) a')
guildmembers_as_list = [] #Since tuples are immutable (cannot append in tuples), this has to be a list (later we convert this list to a tuple)
for names in guild_players(tree): #Placing the data into a list
    guildmembers_as_list.append(names.text)

#Other players, who will be gifted too
with_respected_guildmembers = ["RaiseUrBoobs"]
with_respected_guildmembers.extend(guildmembers_as_list) #Extending the list, so the respected members can be gifted too

#Converting list to tuple
guildmembers = tuple(with_respected_guildmembers)

print(guildmembers) #Returns a tuple, containing all of the players in the guild
print("Total players:",len(guildmembers))
###############################################################################################################################################

#Asking the user to enter the gift code
giftcode = input("Please insert the GiftCode:")

#Going through the whole list of players and submitting their names with the given gift code
for player in guildmembers:
    print(player)
    time.sleep(1.5)
    
    #Checking if the player exists
    playerCheck = requests.post('https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902', data={'ac':'get_extra_info', 'charname': player, 'lang': 'en'})
    print(playerCheck.text)

    #Submitting the gift code
    submitting = requests.post('https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902', data={'ac':'get_gifts', 'type':'1', 'iggid':'0', 'charname': player, 'cdkey': giftcode, 'lang': 'en'})
    print(submitting.text)
