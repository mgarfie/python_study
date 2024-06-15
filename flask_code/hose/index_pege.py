from flask import Blueprint, render_template
from models import House
# 创建蓝图，蓝图的名称为包的名称index_page
index_page = Blueprint('index_page', __name__)

@index_page.route('/index/')

def index():
    # 统计房源信息表中记录条数
    house_total_num = House.query.count()  # 获取房源总数量
    render_template('index.html')

