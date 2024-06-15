from tkinter import *
win = Tk()

win.title("基本按钮设置")
win.geometry("400x200")

# Function

def a():
    print("带入button按钮")


# image---------要在button之前建立，运行顺序的问题
img = PhotoImage(file="E:\\code_python\\创建用户界面\\ico\\lz.png")



# button

but = Button(text="Click name",)
but.config(bg="skyblue")    # 设置颜色
but.config(width=10, height=5)
but.pack()          # 封装以后才会显示
but.config(image= img)                      # 设置图片按钮，图片后缀要用png格式
but.config(command= a())




win.mainloop()