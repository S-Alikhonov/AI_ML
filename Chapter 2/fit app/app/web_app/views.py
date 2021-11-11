import os
import secrets
from logging import log
from flask.helpers import url_for
from flask_wtf import file
from web_app  import app,db,bcrypt
from flask import render_template,request,redirect,flash
from web_app.models import User,Fit_bio
from web_app.form import *
from flask_login import login_user, current_user,logout_user,login_required
from web_app.machine import predicts,rec


#login form
@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('public/index.html')

@app.route('/about')
@login_required
def about():
    return render_template('public/about.html')

#register
@app.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created successfully, you can Log in!','success')
        return redirect(url_for('login'))
    return render_template('public/sign_up.html',title='Sign-up',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('login was unsuccessful! Please check username and password','danger')
    return render_template('public/login_new.html',title='Login',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    image_file = url_for('static',filename='img/'+current_user.image_file)
    info=Fit_bio.query.filter_by(user = current_user).first()

    return render_template('public/account.html',title='account',image_file=image_file,info=info)

@app.route('/account_update',methods=['GET','POST'])
@login_required
def account_update():
    form = PersonalForm()
    info = Fit_bio.query.filter_by(user = current_user).first()
    if form.validate_on_submit():
        w = form.weight.data
        h = form.height.data
        bmi = round(w/(h/100)**2,2)
        
        if info:
            info.age = form.age.data
            info.height = h
            info.weight = w
            info.bmi = bmi
            info.gender = form.gender.data
            current_user.fname =form.fname.data
            current_user.lname = form.lname.data
            db.session.commit()
            flash(f'Your physical info has been updated successfully!','success')
            return redirect(url_for('account'))


        else:
            fit_info = Fit_bio(height=form.height.data,
            weight=form.weight.data,
            gender=form.gender.data,
            age=form.age.data,
            bmi =bmi,
            user=current_user)
            db.session.add(fit_info)
            current_user.fname =form.fname.data
            current_user.lname = form.lname.data
            db.session.commit()
            flash(f'Your physical info has been created successfully!','success')
            return redirect(url_for('account'))
        
    elif request.method =="GET" and current_user.fname and current_user.lname and info:
        
        form.fname.data = current_user.fname
        form.lname.data = current_user.lname
        form.height.data = info.height
        form.weight.data = info.weight
        form.gender.data = info.gender
        form.age.data = info.age
        

    return render_template('public/account_update.html',title='change physical information',form=form)
def save_file(form_file):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.split(form_file.filename)
    f_name = random_hex + f_ext
    file_path = os.path.join(app.root_path,'static/uploads',f_name)
    form_file.save(file_path)
    return file_path

@app.route('/task',methods=["GET","POST"])
@login_required
def task():
    form = UploadForm()
    if form.validate_on_submit():
        if form.csv.data:
            csv_file = save_file(form.csv.data)
            rest = rec(csv_file)
            return render_template('public/new.html',results=rest)    
    return render_template('public/task.html',title='Sync your sensor data',form=form)

# @app.route('/recommend')
# def results():
#     return render_template('public/new.html')
