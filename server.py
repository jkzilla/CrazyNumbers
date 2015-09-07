from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Stats
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Dashboard"""

	return render_template("/dashboard.html")

if __name__ == '__main__':
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)

	app.run()