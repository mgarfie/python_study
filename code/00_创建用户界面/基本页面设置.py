#  import tkinter as tk  # 引入tkinter模块
from tkinter import *   # 引入所有--不太推荐，名称冲突，内容过大，但是可以使用所有
# # 建立主视窗
win = Tk()   # 建立主视窗
win.title("桑战士的快乐生活")


# 定义界面大小

win.geometry("400x200") # 宽×高 这里的x是英文状态的X
# win.minsize(width=400,height=200)   # 最小
# win.maxsize(width=1024,height=768)  # 最大
win.resizable(False,0)          # 宽和高全关闭，就是无法改变大小，0=false 1=true


# 创建图标.ico
win.iconbitmap("小案例\\ico\\sz_1.ico")

# 颜色
win.config(background="skyblue")        # 设置背景色
win.attributes("-alpha", 0.79)      # 1~0 1=100%  0=0%


# 置顶效果
win.attributes("-topmost", 1)       #1= 1置顶 0不置顶

win.mainloop()  # 常驻视窗

