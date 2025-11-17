from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY
from database import db
from routes import bp as main_bp

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="../static")
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["SECRET_KEY"] = SECRET_KEY

    # Inicializa DB
    db.init_app(app)

    # Registra blueprints
    app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Cria as tabelas caso não existam
        from models import Pizza  # noqa: F401
        db.create_all()
    app.run(debug=True, host="127.0.0.1", port=5000)
