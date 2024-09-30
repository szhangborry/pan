from tkinter import *
from tkinter import messagebox
from pyperclip import *
def get1():
    if((mm.get()=="114514") and (zh.get()=="zhangwenzi")):
        messagebox.showinfo("提示","网址为：http://zhangzhenshuai.github.io")
        copy("http://zhangzhenshuai.github.io")
        messagebox.showinfo("提示","网址已复制，请在浏览器中粘贴")
    else:
        messagebox.showinfo("错误","验证失败")
wd=Tk()
wd.geometry("300x130")
wd.title("验证")
Label(wd,text="账号：").grid(row=0,column=0)
Label(wd,text="密码：").grid(row=1,column=0)
mm = Entry(wd,width=25,justify=CENTER,show="*")
zh = Entry(wd,width=25,justify=CENTER)
mm.grid(row=1,column=1,padx=10,pady=5)
zh.grid(row=0,column=1,padx=10,pady=5)
Button(wd,text="提交",width=10,command=get1).grid(row=3,column=0,padx=10,pady=5)
Button(wd,text="退出",width=10,command=wd.quit).grid(row=3,column=1,padx=10,pady=5)
wd.mainloop()