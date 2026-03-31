from flask import Flask
from app.controllers.calculadora_controller import calculadora_bp
from app.controllers.pages_controller import pages_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(calculadora_bp)
    app.register_blueprint(pages_bp)

    return app