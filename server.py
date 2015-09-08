from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Stats
from jinja2 import StrictUndefined
from sqlalchemy import func 
import json

app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Dashboard"""
	data = Stats.query.all()
	data_dict = {}
	x_axis_date_time = []
	y_axis_number = []
	frequency = {}
	for item in data:
		key = int(item.id)
		value = [item.number, str(item.date_time)]
		data_dict[key] = value 

		# print item.number
	json_response = json.load(data_dict)
	print type(json_response)
	return render_template("/dashboard.html", data=data, data_json=data_dict)

if __name__ == '__main__':
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)

	app.run()