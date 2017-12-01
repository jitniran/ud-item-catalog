from flask import Blueprint, render_template
from flask import url_for, request, redirect
from .initdb import session
from models.model import Sport, SportItem

category = Blueprint('category', __name__)


@category.route('/')
@category.route('/catalog')
def catalog():
    """
    method that lists all sports catagories
    """
    sport_catalog = session.query(Sport)
    return render_template('sports/catalog.html', catalog=sport_catalog)


@category.route('/catalog/new', methods=['GET', 'POST'])
def new():
    """
    method for creating new sport
    """
    if(request.method == "POST"):
        name = request.form['name']
        sport = Sport()
        sport.name = name
        session.add(sport)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('sports/new.html')

@category.route('/catalog/<int:sport_id>/edit', methods=['GET', 'POST'])
def edit(sport_id):
    """
    method for creating edit sport
    """
    sport = session.query(Sport).filter_by(id = sport_id).one()
    if(request.method == "POST"):
        name = request.form['name']
        sport.name = name
        session.add(sport)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('sports/edit.html',sport=sport)

