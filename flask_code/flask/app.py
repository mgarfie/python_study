import traceback
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

# 通过URI连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/userdata'
# 动态追踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50))

    def get_name(self):
        return str(self.name)

# 创建数据库表
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin/', methods=['POST', 'GET'])
def signin():

    if request.method == 'GET':
        return render_template("login.html")
    else:
        inputname = request.form.get('input_name')
        inputpassword = request.form.get('input_password')
        print("login", inputname, inputpassword)
        user = User.query.filter_by(name=inputname, password=inputpassword).first()
        if user:
            print('*********')
            return redirect(url_for('index', name=str(inputname)))
        else:
            return redirect(url_for('signup', registered='user or password error'))


@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # ======================注册===================================================
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')
        email = request.form.get('email')
        if password1 == password2:
            user = User(name=name, password=password1, email=email)
            try:
                db.session.add(user)
                db.session.commit()
                print("user", name, email, user)
                return redirect(url_for('signup', registered='true'))
            except IntegrityError as e:
                db.session.rollback()  # 回滚事务

                print('The user or email exists, please try again', 'error')
                return redirect(url_for('signup', registered='user or email exists'))
            except Exception as e:
                db.session.rollback()
                print(traceback.format_exc())
                print('Registration error, please try again', 'error')
                return redirect(url_for('signup', registered='unknown error'))
        else:
            return redirect(url_for('signup', registered='password not match'))



if __name__ == '__main__':
    app.run()
