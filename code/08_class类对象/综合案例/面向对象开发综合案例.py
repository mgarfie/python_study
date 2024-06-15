import json

class data():
    def __init__(self, date, file_id, money, province):
        self.date = date
        self.file_id = file_id
        self.money = money
        self.province = province
    def __str__(self):
        return f"{self.date}, {self.file_id}, {self.money}, {self. province}"


class open_file():
    def open_file(self):
        pass

class textfile(open_file):

    def __init__(self, file):
        self.file = file

    def open_file(self):
        f = open(self.file, "w", encoding="UTF-8")

        record_list = []
        for line in f.readline():
            line = line.strip()                     # 使用strip时，会多一个回车符/n 所以这里要把它代替，使用line是因为要对每一行数据进行处理
            data_list = line.split(",")
            data(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(data)

        f.close()
        return record_list
class jsonfile(open_file):

    def __init__(self, file):
        self.file = file


    def open_file(self):
        f = open(self.file, "r", encoding="UTF-8")

        data_list = []
        for line in f.readline():
            data_dict = json.load(line)
            a = data(data_dict["data"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            data_list.append(a)

        f.close()
        return data_list





