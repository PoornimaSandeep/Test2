from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,SubmitField

class Registration_form(FlaskForm):
      username=StringField(label='username')
      Email=StringField(label='Email')
      Phone_num=IntegerField(label="Phone_number")
      password1=PasswordField(label='Password')
      password2 = PasswordField(label='Confirm_Password')
      Budget=IntegerField(label='Budget')
      submit=SubmitField(label='Create account')
