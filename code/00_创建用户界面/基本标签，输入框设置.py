from tkinter import *
# 创建基本用户界面
win = Tk()
win.geometry("400x200")
win.config(bg="#323232")

# function
def ok():
    t1 = en.get()
    lb.config(text= t1)

# 创建标签
lb = Label(bg="#323232", fg="white", text="word")
lb.pack()

# 创建输入框
en = Entry()
en.pack()
# 创建按钮

but = Button(text="OK", command=ok)
but.pack()
win.mainloop()