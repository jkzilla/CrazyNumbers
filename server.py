from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Stats
from jinja2 import StrictUndefined
from sqlalchemy import func 
import json
import time
from time import strftime, mktime, timezone

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
	chart_js_date_time_labels = []
	for item in data:
		py_date_time = item.date_time
		js_date_time_format = json.dumps(py_date_time.isoformat())
		# print js_date_time_format
		key = int(item.id)
		value = [int(item.number), js_date_time_format]
		data_dict[key] = value 
		y_axis_number.append(int(item.number))
		x_axis_date_time.append(js_date_time_format)
		print type(int(py_date_time.microsecond))
		chart_js_date_time_labels.append(int(py_date_time.microsecond))
	print chart_js_date_time_labels
	# print x_axis_date_time
	# print y_axis_number
	json_response = js_date_time_format
	# print type(json_response)
	
	chart_js3_data = {}
	print type(chart_js_date_time_labels[0])
	chart_js3_data['labels'] = chart_js_date_time_labels
	# print data['labels']
	datasets_dict = {}
	datasets_dict['label'] = "Crazy Numbers"
	datasets_dict['fillColor'] = "rgba(220,220,220,0.5)"
	datasets_dict['strokeColor'] = "rgba(220,220,220,0.8)"
	datasets_dict['highlightFill'] = "rgba(220,220,220,0.75)"
	datasets_dict['highlightStroke'] = "rgba(220,220,220,1)"
	datasets_dict['data'] = y_axis_number
	chart_js3_data['datasets'] = [datasets_dict]
 

	# list_of_dict.append(data)
	# print list_of_dict 	

	return render_template("/dashboard.html", chart_js3_data = chart_js3_data, date_time=x_axis_date_time, number=y_axis_number)

if __name__ == '__main__':
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)

	app.run()