import tkinter as tk
from tkinter import ttk
import database as db

root = tk.Tk()
root.title("Table Switching Program")
root.geometry("1000x700")

menu = tk.Menu(root)
root.config(menu=menu)

menu.add_command(label="Tables", command=lambda: switchSheets(TABLES))
menu.add_command(label="Booking", command=lambda: switchSheets(BOOKINGS))
menu.add_command(label="Guests", command=lambda: switchSheets(GUESTS))

menu.activate(0)

def data_add_decorator(func):
    def wrapper(*args, **kwargs):
        # Add your code here to handle data change in Tkinter treeView
        print("Data in the table has been changed.")
        func(*args, **kwargs)
    return wrapper

def data_delete_decorator(func):
    def wrapper(*args, **kwargs):
        # Add your code here to handle data change in Tkinter treeView
        print("Data in the table has been changed.")
        func(*args, **kwargs)
    return wrapper

class Sheet:
    class Controls:
        frame : tk.Frame

        def __init__(self, master : tk.Frame | tk.Tk, sheet : object) -> None:
            self.frame = tk.Frame(master=master)
            self.entries = []
            self.buttons = []
            self.labels = []

            for i in range(len(sheet.headers)):
                _label = tk.Label(self.frame, text=sheet.headers[i], width=10)
                _label.grid(column=i, row=0)
                self.labels.append(_label)

                _entry = tk.Entry(self.frame, width=20)
                
                _entry.grid(column=i, row=1)
                self.entries.append(_entry)

            self.entries[0].focus = tk.DISABLED
            self.entries[0].insert(0, sheet.database.getValyeById(db.ID) + 1)
            _buttonAddData = tk.Button(self.frame, command=lambda:self.InstertData(sheet=sheet), width=7, text="Добавить")
            _buttonAddData.grid(column=len(sheet.headers), row=1)

            _buttonDeleteData = tk.Button(self.frame, command=lambda:self.DeleteData(sheet=sheet), width=7, text="Удалить")
            _buttonDeleteData.grid(column=len(sheet.headers), row=0)

            self.instertDataBaseValues(sheet=sheet)

            self.frame.pack()
        
        def InstertData(self, sheet) -> None:
            _array = []
            for data in self.entries:
                _array.append(data.get())
            sheet.database.createTable(_array)
            sheet.tree.insert("", "end", values=sheet.database.getValyeById(db.EMPTY))
            self.entries[0].delete(0, tk.END)
            self.entries[0].insert(0, sheet.database.getValyeById(db.ID) + 1)

        def InstertDataValues(self, sheet, values) -> None:
            if values != None:
                sheet.tree.insert("", "end", values=values)

        def DeleteData(self, sheet) -> None:
            selected_item = sheet.tree.selection()
            test = sheet.tree.item(selected_item, option="values")[0]
            test2 = sheet.tree.item(selected_item, option="values")
            sheet.database.deleteTable(sheet.tree.item(selected_item, option="values")[0])
            sheet.tree.delete(selected_item)

        def instertDataBaseValues(self, sheet):
            if sheet.database.getAllTables() == db.EMPTY:
                return 0
            else:
                values = sheet.database.getAllTables()
                for item in values:
                    self.InstertDataValues(sheet=sheet, values=item)



        
    def on_double_click(self, event):
        
        def updateData():
            for i in range(len(self.headers)):
                if _arr[i].get() != None:
                    _data.append(_arr[i].get())
                else:
                    _data.append(item['values'][i])

            self.database.updateTable(_data)
            self.UpdateTable()
            editWindow.destroy()

        item = self.tree.item(self.tree.focus())
        editWindow = tk.Tk()
        editWindow.geometry("700x200")
        _arr = []
        _data = []
        for i in range(len(self.headers)):
            label = tk.Label(master=editWindow, text=self.headers[i], width=10)
            label.grid(column=i, row=0)
            entry = tk.Entry(master=editWindow, width=20)
            entry.insert(0, item['values'][i])
            entry.grid(column=i, row=1)
            _arr.append(entry)

        button = tk.Button(master=editWindow, command=lambda:updateData(), width=7, text="Обновить")
        button.grid(column=len(self.headers) + 1, row=1)

        print("Double-clicked on item:", item['text'])

    frame : tk.Frame
    tree : ttk.Treeview
    headers : list[str]
    controls : Controls
    database : db.Tables | db.Booking | db.Guests

    
    def __init__(self, master : tk.Frame | tk.Tk, table : ttk.Treeview, columns : list[str], database : db.Tables | db.Booking | db.Guests) -> None:
        self.frame = master
        self.tree = table
        self.headers = columns
        self.database = database

        self.HeadingColumns()
        table.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        self.controls = self.Controls(self.frame, self)

        self.tree.bind("<Double-1>", self.on_double_click)



    def HeadingColumns(self, columns : list[str] = None ) -> None:
        if columns == None:
            for i in range(len(self.headers)):
                self.tree.heading(f"#{i+1}", text=self.headers[i])
                self.tree.column(i, minwidth=0, width=100, stretch=tk.NO)

    def UpdateTable(self):
        self.tree.delete(*self.tree.get_children())
        self.controls.instertDataBaseValues(self)


class _TABLES:
    COLUMNS = ('id', 'guestCountMax', 'vipStatus')
    FRAME = tk.Frame(root)
    TABLE = ttk.Treeview(master=FRAME, columns=COLUMNS, show="headings", selectmode="extended")
    DATABASE = db.Tables()
    SHEET = Sheet(master=FRAME, table=TABLE, columns=COLUMNS, database=DATABASE)

class _GUESTS:
    COLUMNS = ('id', 'name', 'surname', 'phone', 'email')
    FRAME = tk.Frame(root)
    TABLE = ttk.Treeview(master=FRAME, columns=COLUMNS, show="headings", selectmode="extended")
    DATABASE = db.Guests()
    SHEET = Sheet(master=FRAME, table=TABLE, columns=COLUMNS, database=DATABASE)

class _BOOKINGS:
    COLUMNS = ('id', 'table_ID', 'guest_ID', 'bookedDate', 'bookedTime', 'guestsCount')
    FRAME = tk.Frame(root)
    TABLE = ttk.Treeview(master=FRAME, columns=COLUMNS, show="headings", selectmode="extended")
    DATABASE = db.Booking()
    SHEET = Sheet(master=FRAME, table=TABLE, columns=COLUMNS, database=DATABASE)


TABLES = _TABLES
GUESTS = _GUESTS
BOOKINGS = _BOOKINGS

sheets = [TABLES, GUESTS, BOOKINGS]

def switchSheets(sheet : TABLES | GUESTS | BOOKINGS):
    for item in sheets:
        item.FRAME.pack_forget()
    sheet.SHEET.UpdateTable()
    sheet.FRAME.pack(expand=tk.YES, fill=tk.BOTH)







