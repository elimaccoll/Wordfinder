# import tkinter as tk
#
# root = tk.Tk()            #Creating the root window
# var = tk.IntVar()         #Creating a variable which will track the selected checkbutton
# cb = []                   #Empty list which is going to hold all the checkbutton
# for i in range(5):
#     cb.append(tk.Checkbutton(root, onvalue = i, variable = var))
#                           #Creating and adding checkbutton to list
#     cb[i].pack()          #packing the checkbutton
#
# root.mainloop()           #running the main loop

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x80')

def isChecked():
    if cb.get() == 1:
        btn['state'] = NORMAL
        btn.configure(text='Awake!')
    elif cb.get() == 0:
        btn['state'] = DISABLED
        btn.configure(text='Sleeping!')
    else:
        print("error")
cb = IntVar()

Checkbutton(ws, text="accept T&C", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()
btn = Button(ws, text='Sleeping!', state=DISABLED, padx=20, pady=5)
btn.pack()

ws.mainloop()