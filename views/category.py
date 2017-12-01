from flask import Blueprint, render_template
from .initdb import session

category = Blueprint('category', __name__,
                    template_folder='templates/catalog')

@category.route('/')
def root():
    return 'main page'

@category.route('/catalog')
def catalog():
    return 'hello'

@category.route('/catalog/new')
def new():
    return render_template('new')
