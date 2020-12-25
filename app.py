from flask import Flask

import views
from models import db
from settings import Config


def create_app(config_object=Config):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    app.config['SECRET_KEY'] = 'dsjm83838mckejcIJDI3j'
    register_blueprints(app=app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


def register_blueprints(app):
    app.register_blueprint(views.page)


if __name__ == '__main__':
    app = create_app()
    app.run()
