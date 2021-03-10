from flask import render_template

from app import app
from app.models.online_shop import orders

@app.route('/orders')
def index():
    return render_template(
        'order.html',
        title='Drinkz R Us',
        orders= orders
    )

@app.route('/orders/<index>')
def show_by_id(index):
    return render_template(
        'find_order.html',
        title='Drinkz R Us',
        index=index,
        orders=orders
    )