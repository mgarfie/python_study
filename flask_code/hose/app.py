from flask import Flask, render_template
from settings import Config
from index_pege import index_page
app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(index_page)            # 注册蓝图index_page
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
