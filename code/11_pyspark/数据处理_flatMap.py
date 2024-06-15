from pyspark import SparkConf, SparkContext
# 给解释器说明python在哪里
import os
os.environ['PYSPARK_PYTHON'] = "E:\\python3.10.4\\python.exe"



# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)



# 区别就在于多解除一层嵌套的功能
rdd = sc.parallelize(["wfgwfwwrg asd a", "iwerewr", "asda sd"])

rdd1 = rdd.flatMap(lambda x: x.split(" "))

print(rdd1.collect())


sc.stop()