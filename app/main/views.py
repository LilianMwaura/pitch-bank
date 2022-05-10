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

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
       
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
    
        db.session.add(new_user)
        db.session.commit()
        return redirect('/success')
    return render_template('signup.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))
         
        return redirect('failure')
    
  
    return render_template('login.html', form=form )

@main.route('/success')
def success():
    
    return render_template('success.html')

@main.route('/failure')
def failure():
    
    return render_template('failure.html')

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    pitch = Pitch.query.all()
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(owner_id=current_user.id, content=form.content.data)
        form.content.data = ''
       
        
        db.session.add(comment)
        db.session.commit()
    return render_template('dashboard.html', name=current_user.username, pitch=pitch, form=form, content=form.content.data)

@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def pitch():
    form = PitchForm()
    
    if form.validate_on_submit():
        pitch = Pitch(owner_id=current_user.id, title=form.title.data, category=form.category.data, description=form.description.data)
        form.title.data = ''
        form.category.data = ''
        form.description.data = ''
        
        db.session.add(pitch)
        db.session.commit()
    return render_template('pitch.html', form=form)

@main.route('/profile')
@login_required
def profile():
    
    pitch = Pitch.query.filter_by(id=current_user.id).all()
    
    return render_template('profile.html', name=current_user.username, email=current_user.email, password=current_user.password, pitch=pitch)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))