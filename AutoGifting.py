import time
import requests

giftcode = input("Please insert the GiftCode:")

guild = ("RaiseUrBoobs", "Bad Juju 4 U", "Otermaster", "vanillebaer", "iTzLife", "ADLER", "scorpionn1", "Tccc", "SpikeyMan", "Ozkopf", "Monkey Butt", "Sizalael", "Lt Kong", "Boindil", "Avaloch II", "Felix Ripper", "drasko 111", "Sozer I", "killerferret", "Squeaks", "Inf4dayz", "BoendalI", "Wootootoo", "Dromadaire", "Bottom 14", "Munchee", "ItsJujuBltch", "CaptainPeace", "Babalon", "chumbeke", "littleguy12", "marky t4", "SSJ Goldbug", "Addo X", "ROGER250891", "Chipset", "KnuffelSammy", "Davaron", "Chaos Enigma", "Ligma Ween", "MilkLover", "The Crippler", "marky1704", "BabyDant", "scorpionn2", "zeeroo1", "Stan S", "rock8383", "Neptunetwo", "mmusic93", "Goldbug", "Crixilicious", "Vuggati", "Calhoun714", "music93", "Ambarhane", "Token Inmate", "S1eeper", "annie 96", "Loony Goony", "BoredOwl", "Mad4 6", "Fapperino", "funkykya", "BonesMcCoy", "Mine Fieldz", "LadyDayana", "Big Meanie", "MrScotty", "Goldbugs Dad", "Goldbugs Mom", "Sizzor", "Jasper2", "Wheatbug", "Metalbug", "Add Stone", "scorpionn4", "Warzone911", "marky1704 2", "Add Food", "Add Wood", "FoodPro Mini", "Add Ore")

#Going through the whole list of players
for player in guild:
    print(player)
    time.sleep(1.5)
    
    #Checking if the player exists
    playerCheck = requests.post('https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902', data={'ac':'get_extra_info', 'charname': player, 'lang': 'en'})
    print(playerCheck.text)

    #Submitting the gift code
    submitting = requests.post('https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902', data={'ac':'get_gifts', 'type':'1', 'iggid':'0', 'charname': player, 'cdkey': giftcode, 'lang': 'en'})
    print(submitting.text)