from flask import Blueprint, render_template, request, session, current_app

calendar_bp = Blueprint('calendar', __name__)

# route to the calendar page 
calendar_bp.route('/calendar', methods = ['GET'])
def calendar():
    """Render the calendar page"""
    render_template("calendar.html")