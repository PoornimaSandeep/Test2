from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

class item(db.Model):
      ID=db.Column(db.Integer(),primary_key=True)
      name=db.Column(db.String(length=10),nullable=False,unique=True)
      barcode=db.Column(db.Integer(),nullable=True)
      price=db.Column(db.Integer(),default=100)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/market")
def market():
    items=[
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html',items=items)

@app.route("/about/<user>")
def about(user):
    return f"<h2>welcome to your page  {user}<h2>"