from flask import Flask, Blueprint, render_template, redirect, url_for
from . import auth, main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.register_blueprint(main)

    @app.route('/home')
    @app.route('/')
    def home():
        return render_template('home.html')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)