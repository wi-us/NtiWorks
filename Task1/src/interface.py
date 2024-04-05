from tkinter import *
from tkinter import ttk
from currency import *
import copy

def doConvert(intName1, value1, intName2):
    obj1 = Currencies.findCurrency(intName1)
    obj2 = Currencies.findCurrency(intName2)
    eurVal1 = obj1.convertToEuro(value1)
    value2 = obj2.convertEuroToCurrency(eurVal1)

    return {"intName1":obj1.intName, "amount1":value1,"intName2":obj2.intName, "amount2":value2}

def showResults():
    result = doConvert(str(currencies_var1.get())[0:3], float(fieldValue1.get()), str(currencies_var2.get())[0:3])
    comboBox1.set(result["intName1"])
    fieldValue1.delete(0, END)
    fieldValue1.insert(0, result["amount1"])
    comboBox2.set(result["intName2"])
    fieldValue2.delete(0, END)
    fieldValue2.insert(0, result["amount2"])


cbVal1 = 0
cbVal2 = 1


def callback(eventObject):
    showResults()

Currencies.doDictionary()
arrNames1 = []
arrNames2 = []

for item in currenciesArray:
    arrNames1.append(item.intName + "," + item.symbol)
    arrNames2.append(item.intName + "," + item.symbol)


root = Tk()
root.geometry("400x85")
root.title("Конвертатор 3000")
frame = Frame(master=root)

labelName1 = Label(master=frame)
labelName2 = Label(master=frame)

currencies_var1 = StringVar(value=arrNames1[0])
currencies_var2 = StringVar(value=arrNames2[1])

print(currencies_var1.get())
print(currencies_var2.get())


comboBox1 = ttk.Combobox(master=frame, textvariable=currencies_var1, values=arrNames1, state='readonly', width=10, name="leftOne")
comboBox2 = ttk.Combobox(master=frame, textvariable=currencies_var2, values=arrNames2, state='readonly', width=10, name="rightOne")

labelEqual = Label(master=frame, text="=", width=1)

fieldValue1 = Entry(master=frame, width=10)
fieldValue2 = Entry(master=frame, width=10)
fieldValue1.insert(0, "1")
showResults()
fieldValue2.insert(0, "0")

buttonDoMagic = Button(master=frame, text="Конвертировать", width=30, name="magic", command=showResults)

comboBox1.bind("<<ComboboxSelected>>", lambda _:callback("leftOne"))
comboBox2.bind("<<ComboboxSelected>>", lambda _:callback("rightOne"))


comboBox1.grid(column=0,row=0, padx=4)
fieldValue1.grid(column=1,row=0, padx=4)
labelEqual.grid(column=2,row=0, padx=4)
comboBox2.grid(column=3,row=0, padx=4)
fieldValue2.grid(column=4,row=0, padx=4)
buttonDoMagic.grid(column=1,row=1, columnspan=3, padx=4, pady=10)

frame.pack(anchor='center', padx=10, pady=10)