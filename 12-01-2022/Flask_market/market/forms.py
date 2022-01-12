from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,data_required,ValidationError
from market.models import user

class Registration_form(FlaskForm):
      def validate_username(self,username_to_check):
          User=user.query.filter_by(name=username_to_check.data).first()
          if User:
             raise ValidationError("Username already exists!! please use different username")

      def validate_Email(self, Email_addres_check):
            User = user.query.filter_by(email= Email_addres_check.data).first()
            if User:
               raise ValidationError("Email already exists!! please use different email")
      username=StringField(label='username',validators=[Length(min=2,max=30),data_required()])
      Email=StringField(label='Email',validators=[Email(),data_required()])
      #Phone_num=IntegerField(label="Phone_number")
      password1=PasswordField(label='Password',validators=[Length(min=6),data_required()])
      password2 =PasswordField(label='Confirm_Password',validators=[EqualTo('password1'),data_required()])
      submit=SubmitField(label='Create account')


class Login_form(FlaskForm):
      username = StringField(label='username', validators=[data_required()])
      password = PasswordField(label='Password', validators=[data_required()])
      submit = SubmitField(label='Sign in')
