from flask import render_template,request,redirect,url_for
from . import main
from flask_wtf import FlaskForm
from .forms import LoginForm, RegisterForm, PitchForm, CommentForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from ..models import Users,Pitch,Comment
from .. import db

@main.route("/")
def index ():
    return render_template("index.html")
