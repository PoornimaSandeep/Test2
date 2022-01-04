from market import app
from flask import render_template
from market.models import item
from market.forms import Registration_form

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/market")
def market():
    items=item.query.all()
    return render_template('market.html',items=items)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/Register")
def register():
    form=Registration_form()
    return render_template('registration.html',form=form)
