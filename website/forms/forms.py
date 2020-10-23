from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models.models import Leden

class RegistrationForm(FlaskForm):
	voornaam = StringField('Voornaam', 
					validators=[DataRequired(), Length(min=2, max=30)])
	achternaam = StringField('Achternaam', 
					validators=[DataRequired(), Length(min=2, max=30)])
	email = StringField('Email',
		validators=[DataRequired(), Email()]) 	
	password = PasswordField('Wachtwoord', 
		validators=[DataRequired()])
	confirm_password = PasswordField('Wachtwoord bevestigen',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Registreer')

	def validate_email(self, email):
		user = Leden.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('De email die u heeft ingevoerd is al in gebruik. Kies een andere email.')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[DataRequired(), Email()]) 	
	password = PasswordField('Wachtwoord', 
		validators=[DataRequired()])
	remember = BooleanField('Mij onthouden')
	submit = SubmitField('Inloggen')


