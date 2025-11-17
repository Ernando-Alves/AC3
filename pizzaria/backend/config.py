import os

# Configurações básicas
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configurações do banco
DB_USER = os.environ.get("DB_USER", "pizzaria_user")
DB_PASS = os.environ.get("DB_PASS", "2025Polola")
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_NAME = os.environ.get("DB_NAME", "pizzaria_db")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get("SECRET_KEY", "troque_esta_chave_para_producao")
