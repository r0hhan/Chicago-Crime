from app import app
from flask import render_template, request, redirect, url_for, session
import requests, json
import connect

@app.route("/")
@app.route("/index/")
def index():
	return render_template('index.html')

@app.route("/compare/")
def compare():
	return render_template('compare.html')

if __name__ == '__main__':
	app.run()
