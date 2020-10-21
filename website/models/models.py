from datetime import datetime
from .. import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return Leden.query.get(int(user_id))

#create db model
#each class represents one table
class Leden(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)


	# create relationship between two tables example
	# relation runs an additional query on the Model2 table.
	# relation = db.relationship('Model2', backref='thismodel', lazy=True)

	#Create function to return string when we add stuff
	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"