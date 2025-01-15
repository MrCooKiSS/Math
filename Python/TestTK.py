from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x450")
root.title("Matrix")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# scroll = Scrollbar()
# scroll.pack(side=RIGHT, fill=Y)

btn = Label(text="|")
btn.grid(row=0, column=0, rowspan=len(matrix), ipadx=6, ipady=6)
btn = Label(text="|")
btn.grid(row=0, column=len(matrix)+1, rowspan=len(matrix), ipadx=6, ipady=6)

root.mainloop()