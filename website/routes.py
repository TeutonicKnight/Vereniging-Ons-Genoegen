from flask import render_template, flash, url_for, request, redirect
from website import app, db, bcrypt
from flask_wtf.csrf import CSRFProtect
from website.forms.forms import RegistrationForm, LoginForm
from website.models.models import Leden
from flask_login import login_user, current_user, logout_user, login_required
import copy

csrf = CSRFProtect(app)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/vergadering', methods=['GET','POST'])
@login_required
def vergadering():
	if request.method == 'POST':
		if 'aanmelden' in request.form:
			current_user.aanwezig = True
			db.session.commit()
			flash(f'Je hebt je aangemeld voor de vergadering!', 'success')
		elif 'afmelden' in request.form:
			current_user.aanwezig = False
			db.session.commit()
			flash(f'Je hebt je afgemeld voor de vergadering!', 'danger')
	return render_template("vergadering.html", Leden=Leden, current_user=current_user)

@app.route('/leden')
def leden():
	return render_template("leden.html", Leden=Leden)

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
		user = Leden(aanhef=form.aanhef.data, voornaam=form.voornaam.data, achternaam=form.achternaam.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account aangemaakt! U kunt nu inloggen', 'success')
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
			flash('successvol ingelogd!', 'success')
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash('Inloggen mislukt. Controleer uw email en wachtwoord', 'danger')
	return render_template("login.html", form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	if request.method == 'POST':
		db.session.delete(current_user)
		db.session.commit()
		flash(f'Account met succes verwijderd!', 'success')
		return redirect(url_for('index'))
	return render_template("account.html")