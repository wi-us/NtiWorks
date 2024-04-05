from tkinter import *
from seasons import *
from functools import partial

def unpackEverything():
        for items in seasonsArr:
            for item in items.interface:
                for obj in item:
                    obj.pack_forget()
        
        for items in mainMenuInterface:
            items.pack_forget()

def switchWindows(seasonName):
    unpackEverything()
    root.geometry("400x650")    
    for items in seasonsArr:
        if items.name == seasonName:
            for item in items.interface:
                    for obj in item:
                        if obj.widgetName == "button":
                            obj.pack(side=TOP, ipady=10, pady=30)
                            
                        if obj.widgetName == "frame":
                            obj.pack(fill=BOTH, expand=True)
                        else:
                            obj.pack(fill=BOTH)

def backToTitle():
    unpackEverything()
    root.geometry("400x400")    
    for items in mainMenuInterface:
            if items.widgetName == "frame":
                items.pack(fill=BOTH, ipady=10, pady=10, expand=True)
            else:
                items.pack(fill=BOTH, ipady=10, pady=10)

root = Tk()
root.title("Когда уже лето?")
root.geometry("400x300")
root.resizable(False, False)

frameTitle = Frame(master=root, padx=60, pady=15, background='pink')
mainMenuInterface = []
mainMenuInterface.append(frameTitle)
for s in seasonsArr:

    frameSeasonTitle = Frame(master=root, width=570, height=570, padx=60, pady=60, name="_" + s.name + "_frameTitle", bg=s.color)
    #frameSeasonDescription = Frame(master=root, width=570, height=570, padx=15, pady=15, name="_" + s.name + "_frameDescription", bg=s.color)

    labelSeasonTitle = Label(master=frameSeasonTitle, text=s.name, name="_" + s.name + "_labelTitle", bg=s.color, font=("Arial", 14))
    labelSeasonDescription = Label(master=frameSeasonTitle, text=s.description, name="_" + s.name + "_labelDescription", wraplength=200, bg=s.color, font=("Arial", 10))

    buttonSeason = Button(master=frameTitle, text=s.name, name="_" + s.name + "_buttonSeason", command=partial(switchWindows, s.name), bg=s.color)
    buttonBackToTitle = Button(master=frameSeasonTitle, text="Back", name="_" + s.name + "_buttonBackToTitle", command=backToTitle, bg=s.color)

    #frameSeasonTitle.pack()
    #frameSeasonDescription.pack()
    #labelSeasonTitle.pack()
    #labelSeasonDescription.pack()
    buttonSeason.pack(fill=BOTH, ipady=10, pady=10)
    
    #buttonBackToTitle.pack()

    interfaceSeason = []
    interfaceSeason.append(frameSeasonTitle)
    #interfaceSeason.append(frameSeasonDescription)
    interfaceSeason.append(labelSeasonTitle)
    interfaceSeason.append(labelSeasonDescription)
    interfaceSeason.append(buttonBackToTitle)
    s.interface.append(interfaceSeason)
    mainMenuInterface.append(buttonSeason)

frameTitle.pack(fill=BOTH, side=TOP, expand=True)