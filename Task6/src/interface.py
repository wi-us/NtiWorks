from tkinter import ttk
from tkinter import *

things = []

class Thing:

    #frame : ttk.Frame
    table : ttk.Treeview
    #headers : list[str]
    visible = False

    def __init__(self, frame : Frame, headers : list[str]) -> None:
        self.frame = frame
        self.headers = headers
        self.table = self.createTable(master=self.frame)
        self.table.grid(row=0, column=0, columnspan=6)

    def createTable(self, master : Frame):
        return ttk.Treeview(master=master, columns=self.headers, show="headings")

    def addRow(table : ttk.Treeview,  value : str):
        table.insert(index=END, values=value)

    def deleteRow(table : ttk.Treeview,  index : int):
        table.delete(table.item(index))

    def frameVisible(self, isVisible : bool):
        if isVisible:
            self.frame.pack()
            self.visible = True
        else:
            self.frame.pack_forget()
            self.visible = False


def changeVisible(objToEnable : Thing):
    for obj in things:
        obj.frameVisible(False)

    objToEnable.frameVisible(True)

def show_frame(frame : Frame):
    frame.tkraise()

root = Tk()
root.title("Orders")
root.geometry("600x600")


pageTables = Thing(
    frame = Frame(master=root, width=600, height=600, bg="#007FFF"),
    headers=['id', 'guestCountMax', 'vipStatus'])

pageBooking = Thing(
    frame = Frame(master=root, width=600, height=600, bg="#A52A2A"),
    headers=['id', 'table_ID', 'guest_ID', 'bookedDate', 'bookedTime', 'guestsCount'])

pageGuests = Thing(
    frame = Frame(master=root, width=600, height=600, bg="#E3CF57"),
    headers=['id', 'name', 'surname', 'phone', 'email'])

things.append(pageTables)
things.append(pageBooking)
things.append(pageGuests)

mainmenu = Menu(root)
root.config(menu=mainmenu)

#mainmenu.add_command(label='Tables', command=lambda:show_frame(pageTables.frame))
#mainmenu.add_command(label='Booking', command=lambda:show_frame(pageBooking.frame))
#mainmenu.add_command(label='Guests', command=lambda:show_frame(pageGuests.frame))

mainmenu.add_command(label='Tables', command=lambda:changeVisible(pageTables))
mainmenu.add_command(label='Booking', command=lambda:changeVisible(pageBooking))
mainmenu.add_command(label='Guests', command=lambda:changeVisible(pageGuests))


btn = Button(master=root, command=pageTables.frame.pack())
btn.pack()
