import tkinter as tk
import tkinter.messagebox as tkmb
from steam.client import SteamClient
from dota2.client import Dota2Client
import dota2.proto_enums as en
import dota2.protobufs.dota_gcmessages_client_match_management_pb2 as asd1
import d2api.src.util as dapi


botStatus = "Offline"
lobbyName = "KS_Test"
lobbyPass = "555"
lobbyMode = en.DOTA_GameMode.DOTA_GAMEMODE_AP
lobbyParticipantsCount = 0

client = SteamClient()
dota = Dota2Client(client)

@client.on('logged_on')
def start_dota():
    dota.launch()


@dota.on('ready')
def do_dota_stuff():
    global botStatus
    botStatus = "Online"
    dota.create_practice_lobby(password=lobbyPass, options={'game_name': lobbyName, "game_mode": lobbyMode})
    dota.invite_to_lobby(steam_id=76561198141995108)

window = tk.Tk()
window.geometry("200x400")
frame1 = tk.Frame(master=window, width=10, height=30)
labelStatus = tk.Label(master=frame1, width=100, height=1, text=f"Status: {botStatus}")
labelLobbyName = tk.Label(master=frame1, width=100, height=1, text=f"Name: {lobbyName}")
labelLobbyPass = tk.Label(master=frame1, width=100, height=1, text=f"Pass: {lobbyPass}")
labelLobbyMode = tk.Label(master=frame1, width=100, height=1, text=f"Mode: {lobbyMode}")
labelLobbyParticipantsCount = tk.Label(master=frame1, width=1, height=1, text=f"Count: {lobbyParticipantsCount}")

frame1.grid(column=0, row=0)
labelStatus.grid(column=0, row=1)
labelLobbyName.grid(column=0, row=2)
labelLobbyPass.grid(column=0, row=3)
labelLobbyMode.grid(column=0, row=4)
labelLobbyParticipantsCount.grid(column=0, row=5)

frame2 = tk.Frame(master=window, width=10, height=30)
labelInviteMember = tk.Label(master=frame2, width=10, height=1, text="SteamID64:")
entryInviteMember = tk.Entry(master=frame2, width=20)
buttonLogin = tk.Button(master=frame2, width=10, height=1, text="Login")
buttonInviteMember = tk.Button(master=frame2, width=10, height=1, text="Invite")

def buttonInviteMember_Click(event):
    dota.invite_to_lobby(int(entryInviteMember.get()))

def buttonLogin_Click(event):
    client.cli_login(username="wiusTheBest", password="9089241034Varav")
    client.run_forever()

buttonLogin.bind("<Button-1>", buttonLogin_Click)
buttonInviteMember.bind("<Button-1>", buttonInviteMember_Click)

frame2.grid(column=0, row=1)
labelInviteMember.grid(column=0, row=0)
entryInviteMember.grid(column=1, row=0)
buttonLogin.grid(column=2, row=0)
buttonInviteMember.grid(column=3, row=0)

def on_closing():
    if tkmb.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        client.disconnect()
        exit()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
