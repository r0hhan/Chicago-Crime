from app import app
from flask import render_template, request, redirect, url_for, session
import requests, json
import connect

@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		tuples = connect.getAll()
		return render_template('index.html', tuples=tuples)
	return render_template('index.html')

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
