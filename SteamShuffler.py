import urllib.request
import random
import re
import os


#Get Your API Key Here: https://steamcommunity.com/dev/apikey
SteamAPIKey = 'EnterYourSteamApiKeyHere!!!'
#Get Your Steam ID Here in the url if you are logged in: http://steamcommunity.com/my
SteamID = 'EnterYourSteamIDHere!!!'


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def keyAndIdCheck():
    if SteamAPIKey == 'EnterYourSteamApiKeyHere!!!' or SteamID == 'EnterYourSteamIDHere!!!':
        print ("Please edit this file and enter your Steam API Key and Steam ID at the top!")
        exit()

def getOwnedGames():
    # Construct API request
    api_request = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + SteamAPIKey + '&steamid=' + SteamID + '&format=json'

    response = urllib.request.urlopen(api_request).read()

    # Convert response to string
    response = response.decode('utf-8')
    return response
    

def findAppids(input_string):
    pattern = r'"appid":(\d+)'
    appids = re.findall(pattern, input_string)

    return appids


def selectRandomGame(appids):
    return random.choice(appids)

def getGameName(appid):
    api_request = 'https://store.steampowered.com/api/appdetails?appids=' + appid
    response = urllib.request.urlopen(api_request).read()
    response = response.decode('utf-8')
    response= re.search('"name":"(.*?)"', response).group(1)
    return response


def main():
    cls()
    keyAndIdCheck()

    print ("""
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⢿⣶⡄⠀⠀⠀⠀⠀⢀⣴⣾⠿⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠻⣿⣆⠀⠀⠀⢠⣿⡟⠁⠀⠀⠙⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⠋⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⠇⠀⠀⠀⠀⠀⠀⠀⢧⠿⣧⠿⣴⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠀⠀⠀⠀
⢰⣿⣿⣿⣿⣧⣤⠀⠀⠀⢀⣀⠀⠀⠀⠀⣤⡀⠀⠀⠀⣀⡀⠀⠀⠀⣤⣼⣿⣿⣿⣿⡆
⢀⣤⣿⣿⣯⣭⣭⠀⠀⠀⢿⣿⡇⠀⢀⣤⣿⣧⡄⠀⢸⣿⣿⠀⠀⠀⣭⣭⣽⣿⣯⣤⡀
⠘⢻⣿⠏⠉⠉⠉⠀⠀⠀⠈⠉⠀⠀⠀⠉⠉⠉⠁⠀⠀⠉⠁⠀⠀⠀⠉⠉⠉⠙⣿⣿⠃
⢀⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⡄
""")
    print ("You should play " + getGameName(selectRandomGame(findAppids(getOwnedGames()))) + "! \n \n")


main()