from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    # return 'Welcome to My Watchlist!'
    return '<h1>Hello トトロ</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(page)}'

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(f"url for 'hello': {url_for('hello')}")  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(f"url for 'user_page': {url_for('user_page', name='dannie')}") # 输出：/user/dannie
    print(f"url for 'user_page': {url_for('user_page', name='RC')}") # 输出：/user/RC
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'