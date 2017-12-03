from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from .initdb import session
from flask import session as login_session
from models.model import Sport, SportItem
from functools import wraps

item = Blueprint('item', __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash('You are not allowed to access there')
            return redirect('/login')
    return decorated_function


@item.route('/catalog/<int:sport_id>/item/show')
def show(sport_id):
    """
    list all items of a particular sport
    """
    items = session.query(SportItem).filter_by(sport_id=sport_id)
    return render_template('items/show.html', items=items)


@item.route('/catalog/item/<int:item_id>/view')
def view(item_id):
    """
    view one item
    """
    item = session.query(SportItem).filter_by(id=item_id).one_or_none()
    return render_template('items/view.html', item=item)


@item.route('/catalog/<int:sport_id>/item/new', methods=['GET', 'POST'])
@login_required
def new(sport_id):
    """
    create new sport
    """
    sport = session.query(Sport).filter_by(id=sport_id).one_or_none()
    if(request.method == "POST"):
        item = SportItem()
        item.name = request.form['name']
        item.description = request.form['description']
        item.price = request.form['price']
        item.sport = sport
        item.user_id = login_session['user_id']
        session.add(item)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('items/new.html', sport=sport)


@item.route('/catalog/item/<int:item_id>/edit',
            methods=['GET', 'POST'])
@login_required
def edit(item_id):
    """
    edit sport item
    """
    item = session.query(SportItem).filter_by(id=item_id).one_or_none()
    if(item.user_id != login_session['user_id']):
        flash('You are not authorized')
        return redirect(url_for('category.catalog'))
    if(request.method == "POST"):
        item.name = request.form['name']
        item.description = request.form['description']
        item.price = request.form['price']
        session.add(item)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('items/edit.html', item=item)


@item.route('/catalog/item/<int:item_id>/delete',
            methods=['GET', 'POST'])
@login_required
def delete(item_id):
    """
    deletes a item of a sport
    """
    item = session.query(SportItem).filter_by(id=item_id).one_or_none()
    if(item.user_id != login_session['user_id']):
        flash('You are not authorized')
        return redirect(url_for('category.catalog'))
    if(request.method == "POST"):
        # remove sport item and commmit to database
        session.delete(item)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('items/delete.html', item=item)
