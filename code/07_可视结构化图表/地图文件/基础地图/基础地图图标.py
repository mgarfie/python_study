from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

a = Map()
data = [
    ("北京", 90),
    ("上海", 199),
    ("湖南", 2333)
]
a.add("地图", data, "china")

a.render()
