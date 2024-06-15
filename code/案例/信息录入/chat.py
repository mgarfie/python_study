from tkinter import *
from tkinter import ttk


class AverageCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("计算平均值")
        self.master.geometry('1360x600')
        self.font = "宋体 20"
        self.padding = (10, 10, 10, 10)
        self.entry_width = 10
        self.labels = [
            "标准1：", "标准2：", "标准3：", "标准4：", "标准5：",
            "标准6：", "标准7：", "标准8：", "标准9：", "标准10："
        ]
        self.entries = []
        self.tree = None
        self.create_widgets()

    def create_widgets(self):
        self.create_frames()
        self.create_labels_and_entries()
        self.create_table()
        self.create_buttons()

    def create_frames(self):
        # 创建所有的Frame组件
        self.frame1 = Frame(self.master, padx=self.padding[0], pady=self.padding[1])
        self.frame2 = Frame(self.master, padx=self.padding[0], pady=self.padding[1])
        self.frame3 = Frame(self.master, padx=self.padding[0], pady=self.padding[1])
        self.frame4 = Frame(self.master, padx=self.padding[0], pady=self.padding[1])
        self.table_frame = Frame(self.master, padx=self.padding[0], pady=self.padding[1])

        # 将所有的Frame组件放置在主窗口中
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=1)
        self.frame4.grid(row=1, column=0)
        self.table_frame.grid(row=2, column=0, columnspan=2)

    def create_labels_and_entries(self):
        # 创建所有的标签和输入框
        for i, label_text in enumerate(self.labels):
            label = Label(self.frame1, text=label_text, font=self.font)
            label.grid(row=i, column=0)
            entry = Entry(self.frame1, width=self.entry_width)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        for i, label_text in enumerate(self.labels):
            label = Label(self.frame2, text=label_text, font=self.font)
            label.grid(row=i, column=0)
            entry = Entry(self.frame2, width=self.entry_width)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

    def create_table(self):
        # 创建表格
        self.tree = ttk.Treeview(
            self.table_frame,
            columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11')
        )
        self.tree.column('#0', width=100, stretch=NO)
        for i in range(1, 11):
            self.tree.column(f'col{i}', width=100, stretch=NO)

        self.tree.column('col11', width=100, stretch=NO)

        self.tree.heading('#0', text='ID')
        for i, label_text in enumerate(self.labels):
            self.tree.heading(f'col{i+1}', text=label_text)
        self.tree.heading('col11', text='平均分')

        self.tree.grid(row=0, column=0)

    def create_buttons(self):
        # 创建按钮
        insert_button = Button(self.frame3, font=self.font, text="录入", command=self.insert_data)
        insert_button.grid(row=1, column=0)

        delete_button = Button(self.frame4, font=self.font, text="删除", command=self.delete_selected)
        delete_button.grid(row=1, column=1)

    def insert_data(self):
        # 添加数据
        values = []
        for entry in self.entries:
            content = entry.get()
            try:
                number = float(content)
            except ValueError:
                print("Invalid input:", content)
                continue
            values.append(number)
            entry.delete(0, END)

        if len(values) == 0:
            return

        count = sum(values)
        avg = count / len(values)

        row_count = len(self.tree.get_children())
        self.tree.insert('', 'end', text=row_count+1, values=tuple(values+[avg]))



    def delete_selected(self):
        # 删除选中的行
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.delete(item)


if __name__ == '__main__':
    root = Tk()
    app = AverageCalculator(root)
    root.mainloop()