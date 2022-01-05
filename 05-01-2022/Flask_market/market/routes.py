from market import app
from flask import render_template,redirect,url_for
from market.models import item,user
from market.forms import Registration_form
from market import db

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

@app.route("/Register",methods=['POST','GET'])
def register():
    form=Registration_form()
    if form.validate_on_submit():
        user_create=user(name=form.username,Phone_num=form.Phone_num,email=form.Email,password=form.password1,budget=form.Budget)
        user(name="poornima", Phone_num=1990202, email="poor@gmail.com", password=123456, budget=2000)
        db.session.add(user_create)
        db.session.commit()
        return redirect(url_for("market"))

    return render_template('registration.html',form=form)
