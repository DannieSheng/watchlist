# watchlist
This is a toy project using flask following the description in [this book](https://helloflask.com/book/3/)

## Create environment

## Activate environment
```
. env/bin/activate
```

## [Database](https://tutorial.helloflask.com/database/)
[SQLAlchemy](https://www.sqlalchemy.org/)
```
(env) $ flask shell
>>> from app import db
>>> db.create_all()
```

`(env) $ flask initdb` or `(env) $ flask initdb --drop`


Function to create fake data: `forge` (`@app.cli.command()`)
```
(env) $ flask forge
```

## [Optimize Templates](https://tutorial.helloflask.com/template2/)
Use base template (base.html)

## [Form](https://tutorial.helloflask.com/form/)
- Get user inputs
- Specify `method` to be `"post"`  

[`click` package](https://click.palletsprojects.com/en/8.1.x/)

`@app.route('/', methods=['GET', 'POST'])`  
两种方法的请求有不同的处理逻辑：
- 对于 `GET` 请求，返回渲染后的页面；
- 对于 `POST` 请求，则获取提交的表单数据并保存。
	- 为了安全的考虑，一般会使用`POST`请求来提交删除请求，也就是使用表单来实现（而不是创建删除链接）

`from flask import request`  
请求的路径: `request.path`  
请求的方法: `request.method`  
表单数据: `request.form`  
查询字符串: `request.args`

`flash()`函数在内部会把消息存储到 Flask 提供的 session 对象里。session 用来在请求间存储数据，它会把数据签名后存储到浏览器的 Cookie 中
in templates: `get_flashed_messages()`


表单数据验证: [WTForms](https://github.com/wtforms/wtforms)

## [用户认证](https://tutorial.helloflask.com/login/)
`flask_login`
安全存储密码: Werkzeug (one of Flask's dependencies)  
生成管理员账户: `admin` function  
使用扩展[Flask-Login](https://github.com/maxcountryman/flask-login)实现用户认证  
用户登录&登出  
认证保护
- 视图保护 (`login_required`装饰器)




