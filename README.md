# watchlist
This is a toy flask project following the description in [this book](https://helloflask.com/book/3/).

## Create environment

## Activate environment
```
. env/bin/activate
```

## [Templates](https://tutorial.helloflask.com/template/)
template rendering (模版渲染) using [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
`{{ ... }}`: 用来标记变量。
`{% ... %}` 用来标记语句，比如 if 语句，for 语句等。
`{# ... #}` 

`{{ variable|filter }}`
[Jinja2 filters](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters)

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
`flask_login`([Flask-Login](https://flask-login.readthedocs.io/en/latest/))
安全存储密码: Werkzeug (one of Flask's dependencies)  
生成管理员账户: `admin` function  
使用扩展[Flask-Login](https://github.com/maxcountryman/flask-login)实现用户认证  
用户登录&登出  
认证保护
- 视图保护 (`login_required`装饰器)

## [unittest]()

*Working outside of application context* [solution](https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask)


## [Reorganize](https://tutorial.helloflask.com/organize/)
* Previous structure:
```├── .flaskenv
├── app.py
├── test_watchlist.py
├── static
│   ├── favicon.ico
│   ├── images
│   │   ├── avatar.png
│   │   └── totoro.gif
│   └── style.css
└── templates
    ├── 400.html
    ├── 404.html
    ├── 500.html
    ├── base.html
    ├── edit.html
    ├── index.html
    ├── login.html
    └── settings.html
```

* Updated structure
```
├── .flaskenv
├── test_watchlist.py
└── watchlist  # 程序包
    ├── __init__.py      包构造文件，创建程序实例
    ├── commands.py      命令函数
    ├── errors.py        错误处理函数
    ├── models.py        模型类
    ├── views.py         视图函数 (or routes.py)
    ├── static
    │   ├── favicon.ico
    │   ├── images
    │   │   ├── avatar.png
    │   │   └── totoro.gif
    │   └── style.css
    └── templates
        ├── base.html
        ├── edit.html
        ├── errors
        │   ├── 400.html
        │   ├── 404.html
        │   └── 500.html
        ├── index.html
        ├── login.html
        └── settings.html
```

## [Deployment](https://tutorial.helloflask.com/deploy/)
[python-dotenv](https://github.com/theskumar/python-dotenv)

* PythonAnywhere

Refer to [this method](https://help.pythonanywhere.com/pages/RebuildingVirtualenvs/) to create virtual environment on PythonAnywhere

## [TODO: Leave-a-message](https://tutorial.helloflask.com/challenge/)