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
