from tkinter import *
win = Tk()
win.geometry("200x200")
win.title("布局方式")


# /////pack
but = Button(text="test")
but.config(font="黑体 20")
but.pack(side=TOP)
but = Button(text="test")
but.config(font="黑体 20")
but.pack(side=LEFT)
but = Button(text="test")
but.config(font="黑体 20")
but.pack(side=BOTTOM)
but = Button(text="test")
but.config(font="黑体 20")
but.pack(side=RIGHT)



win.mainloop()