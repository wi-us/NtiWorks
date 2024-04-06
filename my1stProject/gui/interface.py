import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
for i in range(9):
    for j in range(9):
        if i == j or i == 0 or j == 0:
            color = "gray"
        else:
            color = "white"
        
        if j < 9:
            entry1 = tk.Entry(root, width=10)
            entry1.grid(row=i, column=j*2, padx=5, pady=5)
        
        label = tk.Label(root, text=f"Team {i+1}", bg=color)
        label.grid(row=i, column=j*2+1, padx=5, pady=5)
