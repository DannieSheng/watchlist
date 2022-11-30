from flask import url_for, render_template, redirect, flash, request
from flask_login import login_user, login_required, logout_user, current_user

from watchlist import app, db
from watchlist.models import User, Movie


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if not current_user.is_authenticated:
            return redirect(url_for('index'))

        # acquire data from form
        title = request.form.get('title')
        year = request.form.get('year')

        # data validation
        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.') # send message to HTML template
            return redirect(url_for('index')) # return to home page

        # save data from form to database
        movie = Movie(title=title, year=year) # create record
        db.session.add(movie) # add to database session
        db.session.commit() # commit session
        flash('Item created.') # show success message
        return redirect(url_for('index')) # return to home page

    # user = User.query.first() # read all users' records
    movies = Movie.query.all() #
    return render_template('index.html', movies=movies)


@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))  # 重定向回对应的编辑页面

        movie.title = title  # 更新标题
        movie.year = year  # 更新年份
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页

    return render_template('edit.html', movie=movie)  # 传入被编辑的电影记录


@app.route('/movie/delete/<int:movie_id>', methods=['POST'])  # 限定只接受 POST 请求
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)  # 获取电影记录
    db.session.delete(movie)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for('index'))  # 重定向回主页


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == "POST":
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        # current_user.name = name
        

        user = User.query.first()
        user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))
    return render_template('settings.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if user.username == username and user.validate_password(password): # check username and password
            login_user(user) # login user
            flash('Login success.')
            return redirect(url_for('index')) # redirect to home page

        flash('Invalid username or password.')
        return redirect(url_for('login')) # redirect to login page

    return render_template('login.html')


@app.route('/logout')
@login_required # used to protect视图
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index')) # redirect to home page
