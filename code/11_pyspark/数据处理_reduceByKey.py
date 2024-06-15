from pyspark import SparkConf, SparkContext
# 给解释器说明python在哪里
import os
os.environ['PYSPARK_PYTHON'] = "E:\\python3.10.4\\python.exe"



# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)





# 针对KV型RDD.自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据（value）的聚合操作
rdd = sc.parallelize([("男", 11), ("男", 19), ("女", 16), ("女", 20)])


rdd1 = rdd.reduceByKey(lambda a, b: a + b)

print(rdd1.collect())









sc.stop()