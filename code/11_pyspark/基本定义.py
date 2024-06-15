from pyspark import SparkConf, SparkContext

# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)

# 打印版本号
# print(sc.version)


# 将python对象加载但spark中国，成为rdd对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})


# 看你面有什么东西
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# =============================读取rdd文件数据============================


rdd = sc.textFile('E:\\my__code\\code_python\\11_pyspark\\1.txt')
print(rdd.collect())








sc.stop()