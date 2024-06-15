import json
from pyecharts.charts import Map
from pyecharts.options import *


# 打开文件
f = open("E:\\code_python\\07_可视结构化图表\\地图文件\全国疫情数据\\疫情.txt", "r", encoding="UTF-8")
# 读取文件
f_data = f.read()
# 关闭文件
f.close()
# 将json 转换为 python字典
data_dict = json.loads(f_data)

# 取省份数据
child_total_data = data_dict['areaTree'][0]['children']

# 遍历所有数据，提出需要的做成图表
child_list = []

for child_data in child_total_data:
    # 省份名称
    child_name = child_data["name"]
    # 该省份的确珍人数
    child_confirm = child_data["total"]["confirm"]
    # 该省份的死亡人数
    child_dead = child_data["total"]["dead"]
    # 该省份的疑似人数
    child_suspect = child_data["total"]["suspect"]
    child_list.append((child_name, child_confirm))

map = Map()
map.add("各省份疫情情况", child_list, "china")
map.render()
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图")
    
)
# 现在的的问题(
#   1.地图没数据
#   2.改变不了全局设置
# )

