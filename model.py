"""Model for CrazyNumbers"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connects to SQLite3 db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///numbers.db'

db = SQLAlchemy(app)

# Defines database model
class Stats(db.Model):
	"""
				Crazy Numbers
		This is a table holding:
		- Number
			- Psuedo-randomly generated numbers
		- DateTime 
			- The date and time the table was generated on 

	"""

	__tablename__ = "numbers"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	number = db.Column(db.Integer, nullable=False)
	date_time = db.Column(db.DateTime)

	def __init__(self, number, date_time):
		self.number = number
		self.date_time = date_time

	def __repr__(self):
		"""Representations of printed values"""

		return "<Stats number_id=%s number=%s date_time=%s>" % (self.number_id, self.number, self.date_time)

# Helper functions

def connect_to_db(app):
	"""Connects the database to the CrazyNumbers Flask application."""

	# Configure to use our SQLite database
	app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///numbers.db'
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	# This allows us to work with the database directly from our server.
	from server import app
	connect_to_db(app)
	print "Connected to DB."