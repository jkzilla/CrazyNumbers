from model import Stats, db, connect_to_db
from server import app

import random
import datetime

DB_URI = "http:///crazynumbers.db"
def seed_numbers_w_datetime():
	"""This function generates 300 random numbers and 300 random DateTime values and loads values into the Stats table in our crazynumbers database."""
	
	print "Generating"

	for number in xrange(0-300):
		print xrange(0-300)
		random_num = random.randomint(0,100)
		date_time = datetime.dateime.now()
		print random_num
		print date_time
		stats_table_values = Stats(number=random_num, date_time=this_date_time)
		db.session.add(stats_table_values)
	db.session.commit()
	
if __name__	== '__main__':
	connect_to_db(app)
	print "Connected to DB."

	db.create_all()
	seed_numbers_w_datetime()