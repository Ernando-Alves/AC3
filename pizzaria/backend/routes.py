from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Pizza
from decimal import Decimal, InvalidOperation

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    # Captura o termo de pesquisa do URL (query parameter 'busca')
    termo = request.args.get("busca", "").strip()
    
    # Inicia a query com ordenação
    query = Pizza.query.order_by(Pizza.criado_em.desc())
    
    if termo:
        # Se houver um termo de pesquisa, aplica o filtro.
        query = query.filter(
            db.or_(
                Pizza.nome.ilike(f"%{termo}%"),
                Pizza.ingredientes.ilike(f"%{termo}%"),
            )
        )
    
    pizzas = query.all()
    
    # Passa o termo para o template para que o campo de busca seja preenchido novamente
    return render_template("index.html", pizzas=pizzas, termo=termo)

@bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        ingredientes = request.form.get("ingredientes", "").strip()
        preco_raw = request.form.get("preco", "0").replace(",", ".").strip()

        if not nome:
            flash("O nome da pizza é obrigatório.", "danger")
            return redirect(url_for("main.cadastro"))

        try:
            preco = Decimal(preco_raw)
        except (InvalidOperation, ValueError):
            flash("Preço inválido. Use formato 0.00", "danger")
            return redirect(url_for("main.cadastro"))

        nova = Pizza(nome=nome, ingredientes=ingredientes, preco=preco)
        db.session.add(nova)
        db.session.commit()
        flash(f"Pizza '{nome}' cadastrada com sucesso.", "success")
        return redirect(url_for("main.index"))

    return render_template("cadastro.html")

@bp.route("/excluir/<int:pizza_id>", methods=["POST"])
def excluir(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    nome = pizza.nome
    db.session.delete(pizza)
    db.session.commit()
    flash(f"Pizza '{nome}' excluída.", "success")
    return redirect(url_for("main.index"))
