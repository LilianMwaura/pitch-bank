from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm, form
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember')
    
class RegisterForm(FlaskForm):
    
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('username',validators=[InputRequired()])   
    password = PasswordField('Password',validators=[InputRequired()])
    
    
class PitchForm(FlaskForm):
    
    title = StringField('Title of pitch',validators=[InputRequired()])
    category = StringField('Category: Innovation, Business or Pickup Line',validators=[InputRequired()])
    description = StringField('Pitch',validators=[InputRequired()], widget=TextArea())
    
class CommentForm(FlaskForm):
    content = StringField('Comment')  