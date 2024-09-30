import tkinter as tk
from tkinter import messagebox
import os
def show_popup():
    global a
    global aa
    a+=1
    if a==17:
        aa = True
    else:
        aa = False
    print(aa)
    print(a)
    messagebox.showinfo("hello,baby!","6") 
aa = False
a = 0    
while True:
    if(aa == True):
        break
    root=tk.Tk()
    root.attributes("-fullscreen",True)
    root.attributes("-alpha",0.01)
    button=tk.Button(root,command=show_popup,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
    button.pack()
    root.mainloop()
os._exit()