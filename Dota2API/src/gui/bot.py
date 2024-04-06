from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.features import Lobby
import dota2.proto_enums as en
import threading
import time

client = SteamClient()
dota = Dota2Client(client)

lobbySettings = {'game_name': "KS_Test", "game_mode": en.DOTA_GameMode.DOTA_GAMEMODE_AP, "pass_key": "5551" }
def editLobbySettings(lobbyName, gameMode, lobbyPass):
    lobbySettings['game_name'] = lobbyName
    lobbySettings['game_mode'] = gameMode
    lobbySettings['pass_key'] = lobbyPass


#@client.on('logged_on')
#def start_dota():
#    dota.launch()
#    #dota.create_practice_lobby(password="555")
#    #dota.invite_to_lobby(76561198864397064)

#@dota.on('ready')
#def do_dota_stuff():
#    botStatus = "Online"
#    dota.create_practice_lobby(password=lobbySettings["pass_key"], options= lobbySettings)
#    dota.invite_to_lobby(steam_id=76561198141995108)


def launch_bot():
    client.cli_login(username="wiusTheBest", password="9089241034Varav")
    client.run_forever()

def login_bot():
    pass

def launch_dota():
    pass

def create_lobby():
    #создать лобби
    #выставить необходимые настройки
    #занять слот тренера или зиртеля
    pass

def finish_work():
    dota.destroy_lobby()
    dota.exit()
    client.disconnect()



def invite():
    dota.invite_to_lobby(steam_id=76561198141995108)

#thr1 = threading.Timer(3.0, function=invite)
#thr1.start()

#launch_bot()
time.sleep(1)
print("Try to log in...", client.on('connection_status'))

for i in range(6):
    launch_bot()
    time.sleep(1)
    if(not client.on('logged_on')):
        time.sleep(10)
    else:
        print("Logged in")
        break

    if i == 5:
        print(f"Failed to log in after {60} seconds")
        exit()

print("Try to launch dota...")
print("Try to launch dota...", dota.on('connection_status'))
for i in range(6):
    dota.launch()    
    time.sleep(1)
    if(not dota.on('ready')):
        time.sleep(10)
    else:
        print("Dota launched!")
        break

    if i == 5:
        print(f"Failed to launch dota after {60} seconds")
        dota.exit()
        client.disconnect()
        exit()

dota.create_practice_lobby(password=lobbySettings["pass_key"], options= lobbySettings)
dota.join_practice_lobby_team(team=en.DOTA_GC_TEAM.NOTEAM)
participants = {
    76561198141995108
}
for user in participants:
    time.sleep(1)
    dota.invite_to_lobby(user)
    time.sleep(1)

if input() == "exit":
        dota.exit()
        client.disconnect()
        exit()