from flask import Flask, render_template, Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/connect')
def connect():
    return render_template('connect.html')
