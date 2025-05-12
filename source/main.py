from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/dashboard')
@main.route('/dash')
def dash():
    return render_template('dash.html')
