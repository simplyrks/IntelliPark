from flask import Flask, render_template, request, redirect
import time
import json
import history.py
app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('itpark.db')
cur=conn.cursor()

cur.execute("SELECT e_id FROM employee")
e_id=cur.fetchall()

id_list=[]

for x in e_id:
	id_list.append(x[0])


@app.route('/')	
def loadingpage():
	return render_template('loadingpage.html')


@app.route('/home/')
def home():	
	return render_template('home.html')

@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/Login/')
def Login():
	return render_template('Login.html')



@app.route('/feedback/')
def feedback():
	return render_template('feedback.html')

@app.route('/about/')
def about():
	return render_template('team.html')

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

@app.route('/floor1/', methods=['GET'])
def floor1():
	conn = sqlite3.connect('itpark.db')
	conn.row_factory = dict_factory
	am = conn.cursor()
	am = conn.execute("SELECT * FROM Plot_Fw")
	res1 = am.fetchall()
	am.close()

	return json.dumps(res1);


@app.route('/floor2/', methods=['GET'])
def floor2():
	conn = sqlite3.connect('itpark.db')
	conn.row_factory = dict_factory
	am = conn.cursor()
	am = conn.execute("SELECT * FROM Plot_Tw")
	res2 = am.fetchall()
	am.close()

	return json.dumps(res2);

@app.route('/floor3/', methods=['GET'])
def floor3():
	conn = sqlite3.connect('itpark.db')
	conn.row_factory = dict_factory
	am = conn.cursor()
	am = conn.execute("SELECT * FROM Plot_V")
	res3 = am.fetchall()
	am.close()

	return json.dumps(res3);

@app.route('/update',methods=['GET', 'POST'])
def update():
	conn = sqlite3.connect('itpark.db')
	if request.method == 'GET':
		id = request.args.get('id')
		p_no = request.args.get('p_no')
		floor = request.args.get('floor')
		print(id)
		print(p_no)
		print(floor)
		v_list=[]
		p_no = int(p_no)
		floor = int(floor)
		cur=conn.cursor()
		

		cur.execute("SELECT id FROM Plot_Fw")
		v_l=cur.fetchall()
		for x in v_l:
			v_list.append(x[0])
		

		cur.execute("SELECT id FROM Plot_Tw")
		v_l=cur.fetchall()
		for x in v_l:
			v_list.append(x[0])
		
		cur.execute("SELECT id FROM Plot_V")
		v_l=cur.fetchall()
		for x in v_l:
			v_list.append(x[0])

		if id in v_list:
			return " Vehicle Already Parked"

		if id in id_list:
			if floor==1:
				cur = conn.cursor()
				am = conn.execute("SELECT id FROM Plot_Fw WHERE P_no=p_no")
				avl = am.fetchall()
				print(avl[p_no][0])
				if avl[p_no][0]==None:
					conn = sqlite3.connect('itpark.db')
					conn.execute("UPDATE Plot_Fw SET id=? WHERE P_no=?",(str(id),p_no))
					conn.commit()
					return "success"
				else:
					return"Parking filled"
			if floor==2:
				cur = conn.cursor()
				am = conn.execute("SELECT id FROM Plot_Tw WHERE P_no=p_no")
				avl = am.fetchall()
				print(avl[p_no][0])
				if avl[p_no][0]==None:
					conn = sqlite3.connect('itpark.db')
					conn.execute("UPDATE Plot_Tw SET id=? WHERE P_no=?",(str(id),p_no))
					conn.commit()
					return "success"
				else:
					return"Parking filled"
			if floor==3:
				cur = conn.cursor()
				am = conn.execute("SELECT id FROM Plot_V WHERE P_no=p_no")
				avl = am.fetchall()
				print(avl[p_no][0])
				if avl[p_no][0]==None:
					conn = sqlite3.connect('itpark.db')
					conn.execute("UPDATE Plot_V SET id=? WHERE P_no=?",(str(id),p_no))
					conn.commit()
					return "success"
				else:
					return"Parking filled"
			else:
				return " Enter Correct Floor"
		else:
			return "Enter Correct ID"
	return redirect('home.html')

@app.route('/delete',methods=['GET', 'POST'])
def delete():
	conn = sqlite3.connect('itpark.db')
	if request.method == 'GET':
		id = request.args.get('id')
		floor = request.args.get('floor')
		id = str(id)
		floor = int(floor)
		print(id)
		v_list=[]

		cur=conn.cursor()
		cur.execute("SELECT id FROM Plot_Fw")
		v_l=cur.fetchall()
		for x in v_l:
			v_list.append(x[0])
		
		cur.execute("SELECT id FROM Plot_Tw")
		v_l=cur.fetchall()
		for x in v_l:
			v_list.append(x[0])
		
		vv_list=[]
		cur.execute("SELECT id FROM Plot_V")
		v_l=cur.fetchall()
		print(v_l)
		for x in v_l:
			vv_list.append(x[0])

		if id in v_list:
			if floor==1:
				conn = sqlite3.connect('itpark.db')
				conn.execute("UPDATE Plot_Fw SET id=? WHERE id=?",(None,str(id)))
				conn.commit()
				return "deleted"
			elif floor==2:
				conn = sqlite3.connect('itpark.db')
				conn.execute("UPDATE Plot_Tw SET id=? WHERE id=?",(None,str(id)))
				conn.commit()
				return "deleted"
			else:
				return "Enter Correct Floor"
		if id in vv_list:
			if floor==3:
				conn = sqlite3.connect('itpark.db')
				conn.execute("UPDATE Plot_V SET id=? WHERE id=?",(None,str(id)))
				conn.commit()
				return "deleted"
			else:
				return " Incorrect Correct floor"
		else:
		 	return "Your vehicle is not in the Parking"
	return redirect('home.html')

history.log_gen()

if __name__ == "__main__":
	app.run(debug=True)