from flask import render_template

from app import app
from app.models.online_shop import orders

@app.route('/')
def home():
    return render_template(
        'index.html',
        title="Drinkz R Us"
    )

@app.route('/orders')
def index():
    return render_template(
        'order.html',
        title='Drinkz R Us - Orders',
        orders= orders
    )

@app.route('/orders/<index>')
def show_by_id(index):
    return render_template(
        'find_order.html',
        title='Drinkz R Us - View Order',
        index=index,
        orders=orders
    )