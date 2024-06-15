from pyspark import SparkConf, SparkContext
# 给解释器说明python在哪里
import os
os.environ['PYSPARK_PYTHON'] = "E:\\python3.10.4\\python.exe"



# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)


rdd = sc.parallelize([1, 2, 1, 1, 2, 3, 3, 4, 5, 6])
# 去除重复数据
rdd1 = rdd.distinct()

print(rdd1.collect())



sc.stop()