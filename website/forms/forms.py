from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models.models import Leden

class RegistrationForm(FlaskForm):
	aanhef = RadioField(choices=[('Mevr.','Mevr.'),('Mr.','Mr.')],
		validators=[DataRequired(message="Vul aub de aanhef in")])
	voornaam = StringField('Voornaam', 
					validators=[DataRequired(message="Dit veld mag niet leeg zijn"), Length(min=2, max=30)])
	achternaam = StringField('Achternaam', 
					validators=[DataRequired(message="Dit veld mag niet leeg zijn"), Length(min=2, max=30)])
	email = StringField('Email',
		validators=[DataRequired(message="Dit veld mag niet leeg zijn"), Email(message="Vul een geldig email adres in")]) 	
	password = PasswordField('Wachtwoord', 
		validators=[DataRequired(message="Dit veld mag niet leeg zijn")])
	confirm_password = PasswordField('Wachtwoord bevestigen',
		validators=[DataRequired(message="Dit veld mag niet leeg zijn"), EqualTo('password', message="wachtwoorden komen niet overeen")])
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


