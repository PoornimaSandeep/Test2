from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database_market.db'
app.config['SECRET_KEY']='7e377ad7d6e167aec2c9d7f1'
db=SQLAlchemy(app)

from market import routes