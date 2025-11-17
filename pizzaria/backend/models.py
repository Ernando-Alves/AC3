from datetime import datetime
from database import db

class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    ingredientes = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric(8, 2), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Pizza {self.id} {self.nome}>"
