from flask import request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.models import User, Movie
from . import login as bp_login


@bp_login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('home.index'))

        flash('Invalid username or password.')
        return redirect(url_for('login'))

    return render_template('login.html')


@bp_login.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('home.index'))
