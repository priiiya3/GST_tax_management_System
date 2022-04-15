from flask import request, redirect, url_for, make_response, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
from Project import app, db, encryption
from Project.models import User


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    # we check if this user email is correct and matches to the one in database
    user = User.query.filter_by(email=email).first()

    # check if this user name is already present and matches to the one in database
    username = User.query.filter_by(name=name).first()

    # if incorrect username, cretae alert
    if not username:
        flash('Incorrect UserName')
        return redirect(url_for('home'))

    # check if email and password is correct
    if not user or not check_password_hash(user.password, password):
        flash('Wrong Password or Email')
        return redirect(url_for('home'))
    
    # if user is tax-payer
    if user.role == "Tax_Payer":
        res = make_response(redirect(url_for('tax_payer_home', id=user.id)))
        res.set_cookie('SiteCookie', encryption(user.id), max_age=60 * 60 * 24)
        return res
    # if user is accountet
    elif user.role == "Accountant":
        res = make_response(redirect(url_for('accountant_home', id=user.id)))
        res.set_cookie('SiteCookie', encryption(user.id), max_age=60 * 60 * 24)
        return res


@app.route('/signup', methods=['POST', 'GET'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    #check if this user is already present in database
    user = User.query.filter_by(email=email).first()

    # if the signed up user account already exist in data base we show alert 
    if user:
        flash('Account already exists')
        # redirect the user to login page
        return redirect(url_for('home'))

    # save the data of new user in database
    new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    # redirect user tp tax_payer home page
    res = make_response(redirect(url_for('tax_payer_home', id=new_user.id)))
    res.set_cookie('SiteCookie', encryption(new_user.id), max_age=60 * 60 * 24)
    
    return res
