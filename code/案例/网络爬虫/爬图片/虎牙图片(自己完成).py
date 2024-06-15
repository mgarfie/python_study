from lxml import etree
from lxml import html
from html.parser import HTMLParser
import requests
from urllib import request
x = requests.get('https://www.huya.com/g/4079')             ## 发送请求-----获取到源码信息（纯文字）
parse_html = etree.HTML(x.text)                             #取出来的数据编译成html------（取出来的是HTML源码文字）   

                                                            # tree3 = html.tostring(parse_html[0],encoding='utf-8').decode('utf-8')
                                                            # print(tree3)                                                                      ----------------查看parse_html的内容
a=parse_html.xpath('//img[@class="pic"]')                   # //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置（取子孙节点）。# @	选取属性。

for b in a:
    url=b.xpath('./@data-original')[0]                      #拿图片地址[0]只是就拿到第一个
    numec=b.xpath('./@title')[0]                            #拿到的图片，用他的名字保存
    print(numec)
    print(url)
    request.urlretrieve(url,r'I:\Download\\'+numec+'.jpg')
                                                            #报错原因---
                                                                # 1.src与data-original（自定义属性）-------懒加载的概念
                                                                        # 1.当访问一个页面的时候，先把img元素或是其他元素的背景图片路径替换成一张大小为1*1px图片的路径(这样就只需请求一次)，当图片出现在浏览器的可视区域内时，才设置图片真正的路径，让图片显示出来。这就是图片懒加载。
                                                                        # 通俗一点：
                                                                        # # 1、就是创建一个自定义属性data-src存放真正需要显示的图片路径，而img自带的src放一张大小为1 * 1px的图片路径。
                                                                        # 2、当页面滚动直至此图片出现在可视区域时，用js取到该图片的data-src的值赋给src。
                                                                                        # ps：自定义属性可以取任何名字
                                                                    #所以src当中，不一定是网址的地址，若不是网址的地址，那么程序将会报错，但data-src就肯定是网络地址
                                                                ##.title与alt========不算报错原因
                                                                    #title功能是表示鼠标在图片上停留时，显示一个悬浮框，其中显示的文字，title是全局属性，提供额外的提示信息，当鼠标滑动到该元素时，显示定义的提示。
                                                                    #alt属性为输出纯文字的参数属性，作用是当HTML元素本身的物件无法被渲染时，就显示alt（替换）文字作为一种补救措施。