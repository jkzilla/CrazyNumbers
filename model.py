from flask_sqlalchemy import SQLAlchemy

# Connects to db
db = SQLAlchemy()

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


	# Helper functions

def connect_to_db(app):
	"""Connects the database to the CrazyNumbers Flask application."""

	# Configure to use our SQLite database
	app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///crazynumbers.db'
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	# This allows us to work with the database directly from our server.

	from server import app
	connect_to_db(app)
	print "Connected to DB."