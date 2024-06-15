#  *_* coding:utf8 *_*
# -*- coding:utf-8 -*-

# 加菲猫
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
win = tk.Tk()
win.title("计算平均值")
win.geometry('1360x600')

# -------------------设置Frame---------------
Frame1 = Frame(win, padding=(10, 10, 90, 10))
Frame2 = Frame(win, padding=(90, 10, 10, 10))
Frame3 = Frame(win, padding=(10, 10, 10, 10))
Frame4 = Frame(win, padding=(10, 10, 10, 10))
tableFrame = Frame(win, padding=(10, 10, 10, 10))
# ------------------Frame1-----------------------
lb1 = Label(Frame1, text="标准1：")
lb1.config(font="仿宋 20")
lb1.grid(row=0, column=0)
lb2 = Label(Frame1, text="标准2：")
lb2.config(font="仿宋 20")
lb2.grid(row=1, column=0)
lb3 = Label(Frame1,text="标准3：")
lb3.config(font="仿宋 20")
lb3.grid(row=2, column=0)
lb4 = Label(Frame1, text="标准4：")
lb4.config(font="仿宋 20")
lb4.grid(row=3, column=0)
lb5 = Label(Frame1, text="标准5：")
lb5.config(font="仿宋 20")
lb5.grid(row=4, column=0)

en1 = Entry(Frame1)
en1.grid(row=0, column=1 )
en2 = Entry(Frame1)
en2.grid(row=1, column=1 )
en3 = Entry(Frame1)
en3.grid(row=2, column=1 )
en4 = Entry(Frame1)
en4.grid(row=3, column=1 )
en5 = Entry(Frame1)
en5.grid(row=4, column=1 )

# ------------------Frame2-----------------------
lb1 = Label(Frame2, text="标准6：")
lb1.config(font="仿宋 20")
lb1.grid(row=0, column=0)
lb2 = Label(Frame2, text="标准7：")
lb2.config(font="仿宋 20")
lb2.grid(row=1, column=0)
lb3 = Label(Frame2,text="标准8：")
lb3.config(font="仿宋 20")
lb3.grid(row=2, column=0)
lb4 = Label(Frame2, text="标准9：")
lb4.config(font="仿宋 20")
lb4.grid(row=3, column=0)
lb5 = Label(Frame2, text="标准10：")
lb5.config(font="仿宋 20")
lb5.grid(row=4, column=0)

en6 = Entry(Frame2)
en6.grid(row=0, column=1 )
en7 = Entry(Frame2)
en7.grid(row=1, column=1 )
en8 = Entry(Frame2)
en8.grid(row=2, column=1 )
en9 = Entry(Frame2)
en9.grid(row=3, column=1 )
en10 = Entry(Frame2)
en10.grid(row=4, column=1 )

# --------------------------添加活动指令-----------------------


# 添加数据
def inster(tree):
    # 创建一个列表来存储所有的Entry组件
    entry_list = [en1, en2, en3, en4, en5, en6, en7, en8, en9, en10]

    # 遍历所有的Entry组件，并获取它们的内容
    values = []
    for entry in entry_list:
        content = entry.get()
        # 将字符串转换为浮点数
        try:
            number = float(content)
        except ValueError:
            print("Invalid input:", content)
            continue

        # 将数字添加到值列表中
        values.append(number)

        # 清空Entry组件的内容
        entry.delete(0, END)

    # 如果值列表为空，则不插入到表格中
    if len(values) == 0:
        return

    # 计算平均值
    count = sum(values)
    avg = count / len(values)

    # 获取当前表格中的行数
    row_count = len(tree.get_children())
    # 将ID、值列表和平均值插入到表格中
    tree.insert('', 'end', text=row_count+1, values=tuple(values+[avg]))

def delete_selected():
    # 获取选中的行
    selected_items = tree.selection()
    # 删除选中的行
    for item in selected_items:
        tree.delete(item)

# ---------------------table----Frema4------------------

tree = ttk.Treeview(tableFrame, columns=( 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11'))
tree.column('#0', width=100, stretch=NO)
tree.column('col1', width=100, stretch=NO)
tree.column('col2', width=100, stretch=NO)
tree.column('col3', width=100, stretch=NO)
tree.column('col4', width=100, stretch=NO)
tree.column('col5', width=100, stretch=NO)
tree.column('col6', width=100, stretch=NO)
tree.column('col7', width=100, stretch=NO)
tree.column('col8', width=100, stretch=NO)
tree.column('col9', width=100, stretch=NO)
tree.column('col10', width=100, stretch=NO)
tree.column('col11', width=100, stretch=NO)
# 设置列标题
tree.heading('#0', text='ID')
tree.heading('col1', text='标准1')
tree.heading('col2', text='标准2')
tree.heading('col3', text='标准3')
tree.heading('col4', text='标准4')
tree.heading('col5', text='标准5')
tree.heading('col6', text='标准6')
tree.heading('col7', text='标准7')
tree.heading('col8', text='标准8')
tree.heading('col9', text='标准9')
tree.heading('col10', text='标准10')
tree.heading('col11', text='平均分')

# 添加数据

tree.grid(row=0,column=0)

# -----------------Frame3---------------
but1 = tk.Button(Frame3, font="宋体 20", text="录入", command=lambda: inster(tree))
but1.config()
but1.grid(row=1, column=0)

but2 = tk.Button(Frame4, font="宋体 20", text="删除", command=delete_selected)
but2.grid(row=1, column=1)



# ------------------Frame布局---------------


Frame1.grid(row=0, column=0, padx=3, pady=10)
Frame2.grid(row=0, column=1, padx=3, pady=10)
Frame3.grid(row=1, column=1, padx=3, pady=10)
Frame4.grid(row=1, column=0, padx=3, pady=10)
tableFrame.grid(row=2, column=0, columnspan=2, padx=5, pady=10)


win.mainloop()