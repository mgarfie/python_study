from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Config():
   DEBUG=False
   # 指定数据库的链接地址
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/house'
   # 压制警告信息
   SQLALCHEMY_TRACK_MODIFICATIONS = True
