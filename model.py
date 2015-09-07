"""Model for CrazyNumbers"""

from flask_sqlalchemy import SQLAlchemy
from server import app

# Connects to SQLite3 db

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

	number_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	number = db.Column(db.Integer, nullable=False)
	date_time = db.Column(db.DateTime)

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

	connect_to_db(app)
	print "Connected to DB."