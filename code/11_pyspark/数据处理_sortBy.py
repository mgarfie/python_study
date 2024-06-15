from pyspark import SparkConf, SparkContext
# 给解释器说明python在哪里
import os
os.environ['PYSPARK_PYTHON'] = "E:\\python3.10.4\\python.exe"



# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)


data = sc.textFile('E:\\my__code\\code_python\\11_pyspark\\2.txt')

rdd = data.flatMap(lambda a: a.split(" "))


# 此时可以将所有的单词都转换为二元元组，key为单词，value为1（方便统计计算）

rdd1 = rdd.map(lambda word: (word, 1))


# 此时就可以看出每个单词出现的次数了
rdd2 = rdd1.reduceByKey(lambda a, b: a + b)

print(rdd2.collect())
# 对结果进行一下排序

rdd3 = rdd2.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(rdd3.collect())



# rdd.sortBy(func，ascending=False，numPartitions=1)

# funC：（T） U：告知按照ndd中的哪个数据进行排序，比知 Lambde x：x[1l 表示按照rdd中的第二列元素进行排序
# ascending True升序 Fa1se降
# numPartitions：用多少分区排序



sc.stop()