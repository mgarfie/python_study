from pyspark import SparkConf, SparkContext
# 给解释器说明python在哪里
import os
os.environ['PYSPARK_PYTHON'] = "E:\\python3.10.4\\python.exe"



# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)

# 将数据处理成rdd数据
rdd1 = sc.parallelize([1, 2, 3, 4, 5])

# def fun(data):
#     return data * 10


rdd2 = rdd1.map(lambda x: x * 10).map(lambda x: x + 5)       # 匿名函数lambda,链式调用

print(rdd2.collect())








sc.stop()