from model import Stats, db, connect_to_db
from server import app
import random
import datetime


def seed_numbers_w_datetime():
	"""This function generates 300 random numbers and 300 random DateTime values and loads values into the Stats table in our crazynumbers database."""
	
	print "Stats"

	for number in xrange(1, 301):
		print xrange(1, 301)
		random_num = random.randint(0,100)
		this_date_time = datetime.datetime.now()
		print random_num
		print this_date_time
		stats_table_values = Stats(number=random_num, date_time=this_date_time)
		db.session.add(stats_table_values)
	# After 300 values, we commit to db
	db.session.commit()


if __name__	== '__main__':
	connect_to_db(app)
	db.create_all()

	seed_numbers_w_datetime()