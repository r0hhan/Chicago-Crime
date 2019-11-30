from app import app
from flask import render_template, request, redirect, url_for, session
import requests, json
import connect

@app.route("/")
@app.route("/index/")
def index():
	return "Hello, World"


if __name__ == '__main__':
	app.run()
