# data = pd.read_csv(path, encoding='ISO-8859-1')
from tkinter import *
import random
import pyperclip
# ////////////创建基本的用户界面///////////////////////#
win = Tk()
win.title("第一个界面程序")
win.geometry("400x230")
win.config(bg="#323232")
a = ""
b = ""
# //////////Function////////////////
def ok():
    user_x = int(en1.get())
    user_y = int(en2.get())
    global a, b
    a = str(random.randint(user_x, user_y))
    b = str(random.randint(user_x, user_y))
    lb_x.config(text="X:"+a),
    lb_y.config(text="y:"+b),
    return a, b
def copy():
    pyperclip.copy("X:"+str(a)+"Y:"+str(b))
# ////////创建标签快1/////////////////////
lb1 = Label(text="随机X,Y坐标", fg="skyblue", bg="#323232")
lb1.config(font="仿宋 15")
lb1.pack()
lb2 = Label(text="最小坐标", fg="white", bg="#323232")
lb2.pack()
# ///////////创建文本框1///////////////
en1 = Entry()
en1.pack()
# ////////创建标签快2/////////////////////
lb3 = Label(text="最大坐标", fg="white", bg="#323232")
lb3.pack()
# ///////////创建文本框2///////////////
en2 = Entry()
en2.pack()
lb_x = Label(text="", fg="white", bg="#323232")
lb_x.pack()
lb_y = Label(text="", fg="white", bg="#323232")
lb_y.pack()
ok_but = Button(text="OK", command=ok)
ok_but.pack()
copy_but = Button(text="复制", command=copy)
copy_but.pack()
win.mainloop()