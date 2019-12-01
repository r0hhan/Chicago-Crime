from app import app
from flask import render_template, request, redirect, url_for, session
import requests, json
import connect

@app.route("/")
@app.route("/index/")
def index():
	return render_template('index.html')

@app.route("/count/")
def count():
	tuples = connect.getTuples()
	return render_template('count.html', tuples = tuples)

@app.route("/compare/")
def compare():
	return render_template('compare.html')

@app.route("/insights/")
def insights():
	return render_template('insights.html')

@app.route("/trends/")
def trends():
	return render_template('trends.html')

if __name__ == '__main__':
	app.run()
