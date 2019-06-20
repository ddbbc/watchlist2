from flask import Blueprint

error = Blueprint('error', __name__, url_prefix='/')

from . import views
