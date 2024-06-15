# 载入json模块
import json                                            # 转换json为列表
from pyecharts.options import TitleOpts, LabelOpts               # 全局设置
from pyecharts.charts import Line                      # 将数据绘制成图标

# 读取数据
f_us = open("E:\\code_python\\07_可视结构化图表\\数据分析\\折线图数据\\美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
f_in = open("E:\\code_python\\07_可视结构化图表\\数据分析\\折线图数据\\印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()
f_jp = open("E:\\code_python\\07_可视结构化图表\\数据分析\\折线图数据\\日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
# 将不符合json的报头给去除
us_data = us_data.replace("jsonp_1629344292311_69436(", "")       # 使用转换函数将报头转换为空
in_data=in_data.replace("jsonp_1629350745930_63180(", "")
jp_data=jp_data.replace("jsonp_1629350871167_29498(", "")
# 去除不符合的包尾
us_data = us_data[:-2]                                  # 这里使用的是切分，因为如果还使用切换函数的话，会将不该转换的数据给转换了。切分到最后两个字符。完成去除包尾
in_data = in_data[:-2]
jp_data = jp_data[:-2]
# json转换为字典
us_dict = json.loads(us_data)
in_dict = json.loads(in_data)
jp_dict = json.loads(jp_data)
# 只要trend中的数据
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 取出数据中日期作为x。在取第一年的数据(下标在314，在www.ab173网址看的)
us_x_data = us_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]

# 取出数据为Y，同样获取到第一年
us_y_data = us_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]

# 生成图表
Line = Line()       # 构建折线图对象
# 创建x轴数据
Line.add_xaxis(us_x_data)       # x轴是共用的，所以随便一个就可以

# 创建y轴数据

Line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))     # 美
Line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))     # 日
Line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))     # 印

# label_opts=LabelOpts(is_show=False) 代表着不显示详细的数据

# 调用render，生成图表
Line.render()
# 设置全局选项
Line.set_global_opts(title_opts=TitleOpts(
    title="老哥示范",
    title_link="http://pyecharts.org/",
    subtitle="老哥太强了",
    pos_left="20%"
))
# 关闭文件
f_jp.close()
f_us.close()
f_in.close()





























