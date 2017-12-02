from flask import (Blueprint, render_template,
                   url_for, request, redirect)
from .initdb import session
from flask import session as login_session
from models.model import Sport, SportItem

item = Blueprint('item', __name__)


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
    item = session.query(SportItem).filter_by(id=item_id).one()
    return render_template('items/view.html', item=item)


@item.route('/catalog/<int:sport_id>/item/new', methods=['GET', 'POST'])
def new(sport_id):
    """
    create new sport
    """
    if 'username' not in login_session:
        return redirect('/login')
    sport = session.query(Sport).filter_by(id=sport_id).one()
    if(request.method == "POST"):
        item = SportItem()
        item.name = request.form['name']
        item.description = request.form['description']
        item.price = request.form['price']
        item.sport = sport
        session.add(item)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('items/new.html', sport=sport)


@item.route('/catalog/item/<int:item_id>/edit',
            methods=['GET', 'POST'])
def edit(item_id):
    """
    edit sport item
    """
    if 'username' not in login_session:
        return redirect('/login')
    item = session.query(SportItem).filter_by(id=item_id).one()
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
def delete(item_id):
    """
    deletes a item of a sport
    """
    if 'username' not in login_session:
        return redirect('/login')
    item = session.query(SportItem).filter_by(id=item_id).one()
    if(request.method == "POST"):
        # remove sport item and commmit to database
        session.delete(item)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('items/delete.html', item=item)
