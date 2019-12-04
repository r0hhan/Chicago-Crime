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

@app.route("/insight/")
def insight():
	pie = connect.s1mple1()
	labels = []
	perc = []
	for x in pie:
		labels.append(x[0][1:-1])
		perc.append(x[1])
	yers = connect.s1mple2()
	wards = connect.complex5()
	return render_template('insight.html', labels=labels, perc=perc, yers=yers, wards=wards)

@app.route("/compare/", methods=['GET', 'POST'])
def compare():
	if request.method == 'POST':
		if request.form['from'] == 'form1':
			low = request.form['low']
			high = request.form['high']
			decline = connect.complex1(low, high)
			decline = decline[0][0]
			text = "Decrease"
			if decline < 0:
				text = "Increase"
			return render_template('compare.html', decline=abs(decline), text=text)
		else:
			low = request.form['low1']
			high = request.form['high1']
			declineList = connect.complex2(low, high)
			print (declineList)
			return render_template('compare.html', declineList=declineList)
	return render_template('compare.html')


@app.route("/trends/", methods=['GET', 'POST'])
def trends():
	data = ['Deceptive Practice', 'Narcotics', 'Burglary', 'Criminal Damage', 'Kidnapping', 'Prostitution', 'Human Trafficking', 'Robbery', 'Crim Sexual Assault', 'Assault', 'Battery Homicide', 'Motor Vehicle Theft', 'Theft', 'Offense Involving Children', 'Weapons Violation']
	if request.method == 'POST':
		if request.form['button'] == 'yearInput':
			year = request.form['time']
			value = connect.complex4(year)
			yData = []
			pDis = []
			for x in value:
				yData.append(x[1])
				pDis.append(x[0])
			return render_template('trends.html', yData = yData, pDis=pDis, value=value, data=data)
		labels = list(range(1, 25))
		crime = request.form.get('crimeSelect')
		value = connect.complex3(crime.upper())
		values = []
		for x in value:
			values.append(x[1])
		return render_template('trends.html', data = data, values=values, labels=labels, crime=crime.title())
	else:
		return render_template('trends.html', data = data)

if __name__ == '__main__':
	app.run()
