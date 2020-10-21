from flask import render_template, flash, url_for, request, redirect
from website import app, db, bcrypt
from website.forms.forms import RegistrationForm, LoginForm
from website.models.models import Leden
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/vergadering')
def vergadering():
	return render_template("vergadering.html")

@app.route('/leden')
def leden():
	return render_template("leden.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Leden(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created! Able to Log in', 'success')
		return redirect(url_for('login'))
	return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Leden.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash('Login unsuccessful please check email and password', 'danger')
	return render_template("login.html", form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
	return render_template("account.html")