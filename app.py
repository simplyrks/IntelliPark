from flask import Flask, render_template
import time

app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('itpark.db')
cur=conn.cursor()


@app.route('/')	
def loadingpage():
	return render_template('loadingpage.html')


@app.route('/home/')
def home():	
	return render_template('home.html')

@app.route('/index/')
def index():
	return render_template('index.html')



@app.route('/feedback/')
def feedback():
	return render_template('feedback.html')

@app.route('/about/')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)