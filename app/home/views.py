from . import home
from flask_login import login_required, current_user
from flask import request, flash, redirect, url_for, render_template
from app.models import db, User, Movie


@home.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('home.settings'))

        current_user.name = name

        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('home.index'))

    return render_template('settings.html')


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if not current_user.is_authenticated:
            return redirect(url_for('home.index'))

        title = request.form.get('title')
        year = request.form.get('year')

        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('home.index'))

        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('home.index'))

    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)


@home.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))

        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('home.index'))

    return render_template('edit.html', movie=movie)


@home.route('/movie/delete/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('home.index'))
