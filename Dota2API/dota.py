from steam.client import SteamClient
from dota2.client import Dota2Client
import dota2.enums as en
import time

client = SteamClient()
dota = Dota2Client(client)
loginStr = "Login"
passStr = "Pass"

loginStr1 = "Login"
passStr1 = "Pass"

options = {"game_name": "KSTest123", "game_mode": en.DOTA_GameMode.DOTA_GAMEMODE_CM}

def getInfoAboutMatch(matchID):
    client.cli_login(username=loginStr1, password=passStr1)
    client.run_forever()
    client.change_status('invisible')
    start_dota()
    do_dota_stuff()

    @client.on('logged_on')
    def start_dota():
        print("Я в стиме")
        dota.launch()

    @dota.on('ready')
    def do_dota_stuff():
        print("Я в доте")
        matchDetail = dota.request_match_details(matchID)
        print("Данные получены")
        open("C://Users//1вин//Documents//MatchDetails.txt", "w+").writelines(matchDetail)
        print("Данные записаны")
        time.sleep(2)
        dota.exit()
        print("Доты всё")
        client.logout()
        print("Я закончил")

def getInfoAboutMatch1(matchID):
    client.cli_login(username=loginStr1, password=passStr1)
    client.run_forever()
    time.sleep(2)
    
    client.change_status('invisible')

    print("Я в стиме")
    time.sleep(1)
    dota.launch()
    print("Я в доте")
    time.sleep(1)
    matchDetail = dota.request_match_details(matchID)
    time.sleep(1)
    print("Данные получены")
    open("C://Users//1вин//Documents//MatchDetails.txt", "w+").writelines(matchDetail)
    print("Данные записаны")
    time.sleep(2)
    dota.exit()
    print("Доты всё")
    time.sleep(1)
    client.logout()
    print("Я закончил")

#getInfoAboutMatch(7623350123)
getInfoAboutMatch1(7623350123)
