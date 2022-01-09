from market import app
from flask import render_template,redirect,url_for,flash
from market.models import item,user
from market.forms import Registration_form,Login_form
from market import db

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/market")
def market():
    items=item.query.all()
    return render_template('market.html',items=items)



@app.route("/Register",methods=['GET','POST'])
def register():
    form=Registration_form()
    if form.validate_on_submit():
        user_create=user(name=form.username.data,
                         email=form.Email.data,
                         password=form.password1.data)
        form.populate_obj(user_create)
        db.create_all()
        db.session.add(user_create)
        db.session.commit()
        return redirect(url_for("market"))
    if form.errors !={}:
        for erro_msg in form.errors.values():
           flash("Error occured is",erro_msg)

    return render_template('registration.html',form=form)

@app.route("/login")
def login():
    form=Login_form()
    return render_template('login.html',form=form)