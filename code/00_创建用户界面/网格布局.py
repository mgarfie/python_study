from tkinter import *
win = Tk()
win.geometry("400x250")
win.title("网格布局")

# grid网格布局
user = Label(text="User:")
user.config(font="Caslon 15")
user.grid(row=0, column=0)

password = Label(text="Password:")
password.config(font="Caslon 15")
password.grid(row=1, column=0,)
# //////////////////////////如果要合并表格则可以使用关键字  v+span///////////////////////////////
# ////一
# user_data = Entry()
# user_data.config(font="Caslon 15")
# user_data.grid(row=0, column=1)
# password_data = Entry()
# password_data.config(font="Caslon 15")      # 在grid里面，输入框的大小取决于你使用的字体与字体大小
# password_data.grid(row=1, column=1)

# ///二----------- rowspan
user_data = Entry()
user_data.config(font="Caslon 30")
user_data.grid(row=0, column=1, rowspan=2)






















win.mainloop()
