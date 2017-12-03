from flask import (Blueprint, render_template,
                   url_for, request, redirect, jsonify)
from .initdb import session
from models.model import Sport, SportItem
from flask import session as login_session

category = Blueprint('category', __name__)


@category.route('/')
@category.route('/catalog')
def catalog():
    """
    lists all sports catagories
    """
    sport_catalog = session.query(Sport).all()
    items = session.query(SportItem).order_by(SportItem.id.desc()).all()
    return render_template('sports/catalog.html', catalog=sport_catalog,
                           items=items)


@category.route('/catalog/new', methods=['GET', 'POST'])
def new():
    """
    create new sport
    """
    if 'username' not in login_session:
        return redirect('/login')
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
    edit sport
    """
    if 'username' not in login_session:
        return redirect('/login')
    sport = session.query(Sport).filter_by(id=sport_id).one()
    if(request.method == "POST"):
        name = request.form['name']
        sport.name = name
        session.add(sport)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('sports/edit.html', sport=sport)


@category.route('/catalog/<int:sport_id>/delete', methods=['GET', 'POST'])
def delete(sport_id):
    """
    deletes sport
    """
    if 'username' not in login_session:
        return redirect('/login')
    sport = session.query(Sport).filter_by(id=sport_id).one()
    if(request.method == "POST"):
        # remove sport items and commmit to database
        session.delete(sport)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('sports/delete.html', sport=sport)

#Json API to view the whole catalog
@category.route('/catalog/JSON')
def catalogJSON():
    """
    makes a json of present catalog
    """
    sports = session.query(Sport).all()
    sport_list = []
    for sport in sports:
        sport_dict = {}
        sport_dict['id'] = sport.id
        sport_dict['name'] = sport.name
        items = session.query(SportItem).filter_by(sport_id=sport.id).all()
        sport_dict['items'] = [i.serialize for i in items]
        sport_list.append(sport_dict)
    return jsonify(catalog=sport_list)
