from pyspark import SparkConf, SparkContext
# 给解释器说明python在哪里
import os
os.environ['PYSPARK_PYTHON'] = "E:\\python3.10.4\\python.exe"



# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# 这个代码的本质就是将数据转换为list列表
rdd_list = rdd1.collect()

print(rdd_list)
print(type(rdd_list))
# reduce求相加的和
rdd2 = rdd1.reduce(lambda a, b: a + b)
print(rdd2)



# take 取几个

take_list = rdd1.take(3)
print(take_list)

# count
count_list = rdd1.count()
print(count_list)

sc.stop()