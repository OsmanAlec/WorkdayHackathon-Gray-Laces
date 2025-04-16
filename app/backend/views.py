#stores the standard roots for the website 

from flask import Blueprint, render_template 

views = Blueprint('views', __name__)

@views.route('/calendar')
def calendar():
    return render_template("calendar.html")

# route for the shop 
views.route('/shop')
def shop():
    return render_template("shop.html")