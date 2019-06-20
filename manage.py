from flask_script import Manager
from app import create_app
import click
from app.models import db, User, Movie
from flask_login import LoginManager

app = create_app()

manager = Manager(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login.login'


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user


@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')


if __name__ == '__main__':
    app.run()
