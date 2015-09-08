from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Stats
from jinja2 import StrictUndefined
from sqlalchemy import func 


app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Dashboard"""
	data = Stats.query.all()
	data_dict = {}
	for item in data:
		key = str(item.id)
		value = [item.number, item.date_time]
		data_dict[key] = value 
		# print item.number
	print len(data_dict)
	# print type(data) this is class model.Stats
	date_time_array = db.session.query(Stats.number).all()
	print type(date_time_array)
	# for number in date_time_array:
	# 	print number
	return render_template("/dashboard.html", data=data)

if __name__ == '__main__':
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)

	app.run()