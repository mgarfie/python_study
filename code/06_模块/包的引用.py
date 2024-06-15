#=================import引入的=======================


import my_package.my_module4       #包的引用与模块并无太大的差异，多了一个父级，当一个文件夹里有__init__.py文件时，他才是一个python包，否则只是一个文件夹
import my_package.my_module6

my_package.my_module4.test()
my_package.my_module6.test()
#===================from引入的=============================

from my_package import my_module4
from my_package import my_module6
my_module4.test()
my_module6.test()
     
from my_package.my_module4 import test
test()
from my_package.my_module6 import test
test()

#而all函数则是在init包里写

from my_package import*
my_module5.test()                                   #就像这样，my_module5是识别不出来的
my_module4.test()