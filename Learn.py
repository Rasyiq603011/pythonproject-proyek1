import os
import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.geometry("500x600")

teks = ""

def text():
    teks.join('+')
    return teks

label = tk.Label(root, text = teks, foreground="white", background="black")
label.pack()


button1 = tk.Button(root, text="tambah", command=text)
button1.pack()

root.mainloop()