from tkinter import *
from src.gui.bot import *

root = Tk()

def on_closing():
    if Tk.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        finish_work()
        exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

root['bg'] = '#fafafa'
root.title = "Steam BOT by wi-us"

frameInfo = Frame(master=root, width=40, height=60, bg='red')
labelBotStatus = Label(master=frameInfo)
labelLobbyStatus = Label(master=frameInfo)
labelUsersCount = Label(master=frameInfo)

frameInfo.pack(side=LEFT)
labelLobbyStatus.pack()
labelLobbyStatus.pack()
labelUsersCount.pack()

frameControls = Frame(master=root, width=40, height=60, bg='green')
buttonLaunchBot = Button(master=frameControls)
buttonLaunchBot.bind("<Button-1>", launch_bot)

root.mainloop()