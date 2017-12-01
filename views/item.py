from flask import (Blueprint, render_template,
url_for, request, redirect)
from .initdb import session
from models.model import Sport, SportItem

item = Blueprint('item', __name__)

@item.route('/catalog/<int:sport_id>/item/new', methods=['GET', 'POST'])
def new(sport_id):
    """
    create new sport
    """
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


@item.route('/catalog/<int:sport_id>/item/<int:item_id>/edit',
            methods=['GET', 'POST'])
def edit(sport_id, item_id):
    """
    edit sport item
    """
    sport = session.query(Sport).filter_by(id=sport_id).one()
    item = session.query(SportItem).filter_by(id=item_id).one()
    if(request.method == "POST"):
        item.name = request.form['name']
        item.description = request.form['description']
        item.price = request.form['price']
        session.add(item)
        session.commit()
        return redirect(url_for('category.catalog'))
    else:
        return render_template('items/edit.html', sport=sport, item=item)


@item.route('/catalog/<int:sport_id>/item/<int:item_id>/delete',
            methods=['GET', 'POST'])
def delete(sport_id, item_id):
    """
    deletes a item of a sport
    """
    sport = session.query(Sport).filter_by(id=sport_id).one()
    item = session.query(SportItem).filter_by(id=item_id).one()
    if(request.method == "POST"):
        # remove sport item and commmit to database
        session.delete(item)
        session.commit()
        return redirect(url_for('item.catalog'))
    else:
        return render_template('sports/delete.html', sport=sport, item=item)
