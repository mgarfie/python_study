from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox as messagebox
class App:
    def __init__(self, win_name):
        self.win_name = win_name
    def win_from(self):
        pass
    def win_Frame(self):
        pass
    def win_table(self):
        pass
    def win_labels_and_entrie(self):
        pass
    def win_but(self):
        pass
    def win_database(self):
        pass
class action_toal():
    def data_int(self):
        pass

    def data_out(self):
        pass

    def data_dele(self):
        pass

    def data_open(self):
        pass
class win(App):

    def __init__(self, win_name):
        self.win_name = win_name

    def win_from(self):
        self.win_name.title("评分专用")
        self.win_name.geometry('900x600')


    def win_labels_and_entrie(self):
        labels_and_entrie = LabelsAndEntrie(self.win_name)
        labels_and_entrie.win_labels_and_entrie()
class _Frame(App):
    def __init__(self, win_name):
        super().__init__(win_name)


    def win_Frame(self):

        self.frame1 = Frame(self.win_name, padding = (270, 10, 10, 10))
        self.frame2 = Frame(self.win_name, padding = (10, 10, 10, 10))
        self.frame3 = Frame(self.win_name, padding = (10, 10, 10, 10))
        self.frame4 = Frame(self.win_name, padding = (10, 10, 10, 10))
        self.frame5 = Frame(self.win_name, padding = (10, 10, 10, 10))

        self.frame1.grid(row=0, column=1, padx=10, pady=10)
        self.frame2.grid(row=0, column=2, padx=10, pady=10)
        self.frame3.grid(row=1, column=2, padx=10, pady=10)
        self.frame4.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        self.frame5.grid(row=2, column=0, columnspan=3, padx=10, pady=20)
entries_list = []
class LabelsAndEntrie(App):
    def __init__(self, win_name):
        super().__init__(win_name)
        self._Frame = _Frame(win_name)
        self.labels = [
            "标准1：", "标准2：", "标准3：", "标准4：", "标准5：",
            "标准6：", "标准7：", "标准8：", "标准9：", "标准10："
        ]
        self.b = "宋体 20"

        self.tree = ttk.Treeview(win_name)
        self.tree.grid(row=0, column=0)

    def win_labels_and_entrie(self):
        self._Frame.win_Frame()
        global entries_list
        entries_list.clear()
        for i, label_text in enumerate(self.labels):
            if i < 5:
                label_frame = self._Frame.frame1
            else:
                label_frame = self._Frame.frame2

            label = Label(label_frame, text=label_text, font=self.b)
            label.grid(row=i, column=0)
            entry = Entry(label_frame, width=10)
            entry.grid(row=i, column=1)

            entries_list.append(entry)

        return entries_list
class _table(App):
    def __init__(self, win_name):
        super().__init__(win_name)
        self._Frame = _Frame(win_name)
        self.LabelsAndEntrie = LabelsAndEntrie(win_name)
        self._Frame.win_Frame()                             # 在 _Frame 类中，虽然定义了 frame5 属性，但是该属性是在 win_Frame 方法中创建的，
                                                            # 而不是在 _Frame 类的 __init__ 方法中创建的。因此，在 win_table 方法中访问 frame5 属性时，
                                                            # 需要先调用 win_Frame 方法来创建该属性。

    #     self.tree = self.win_table()
    # def win_table(self):

        # 创建表格
        self.tree = ttk.Treeview(
            self._Frame.frame5,
            columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11')
        )
        self.tree.column('#0', width=70, stretch=NO)
        for i in range(1, 11):
            self.tree.column(f'col{i}', width=70, stretch=NO)

        self.tree.column('col11', width=70, stretch=NO)

        self.tree.heading('#0', text='ID')
        for i, label_text in enumerate(self.LabelsAndEntrie.labels):
            self.tree.heading(f'col{i+1}', text=label_text)
        self.tree.heading('col11', text='平均分')

        self.tree.grid(row=0, column=0)

class action(App, action_toal):
    def __init__(self, win_name):
        super().__init__(win_name)
        global entries_list
        self.table = _table(win_name)
        self.trr = self.table.tree


    def data_int(self):
        self.trr = self.table.tree
        values = []
        for entry in entries_list:
            content = entry.get()
            if not content:
                print("为空值.")
                continue
            try:
                number = float(content)
            except ValueError:
                print("出错:", content)
                continue
            values.append(number)
            entry.delete(0, END)

        if len(values) == 0:
            return

        count = sum(values)
        avg = count / len(values)

        row_count = len(entries_list)

        values = tuple(values + [avg])
        print(row_count)

        self.trr.insert("", 'end', text=row_count, values=values)
        print(values)
        print(type(values))


class _but(App):

    def __init__(self, win_name):
        super().__init__(win_name)
        self._Frame = _Frame(win_name)
        self.b = "宋体 20"
        self.action = action(win_name)  # 实例化 action 类

    def win_but(self):
        self._Frame.win_Frame()
        but1 = tk.Button(self._Frame.frame3, font=self.b, text="录入", command=self.action.data_int)  # 调用 action 类的 data_int() 方法
        but1.grid(row=0, column=1)

        but2 = tk.Button(self._Frame.frame4, font=self.b, text="删除")
        but2.grid(row=0, column=0)

def activation(a):
    a.win_from()
    a.win_labels_and_entrie()
    a.win_Frame()
    a.win_table()
    a.win_database()
    a.win_but()

if __name__ == '__main__':
    root = Tk()
    run_win = win(root)
    run_but = _but(root)
    run_table = _table(root)

    activation(run_win)
    activation(run_but)
    activation(run_table)
    root.mainloop()
