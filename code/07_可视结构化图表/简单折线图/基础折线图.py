# 导包，导入line功能绘画折线图
from pyecharts.charts import Line

# 导包，设置全局标题
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts
# 得到折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(["中国", "美国", "日本"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])
# 生成图表
line.render()
# 配置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),

)
