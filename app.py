from flask import Flask, render_template, request, redirect
import time
import json
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(email):  
    if(re.search(regex,email)):  
        return True 
    else:  
    	return False
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
			return " Your Vehicle is Already Parked"

		selstring1 = "SELECT id FROM Plot_Fw WHERE P_no = "+str(p_no)+";"
		selstring2 = "SELECT id FROM Plot_Tw WHERE P_no = "+str(p_no)+";"
		selstring3 = "SELECT id FROM Plot_V WHERE P_no = "+str(p_no)+";"

		if id in id_list:
			if floor==1:
				cur = conn.cursor()
				am = conn.execute(selstring1)
				avl = am.fetchall()
				
				
				
				if avl[0][0]==None:
					conn = sqlite3.connect('itpark.db')
					conn.execute("UPDATE Plot_Fw SET id=? WHERE P_no=?",(str(id),p_no))
					conn.commit()
					return "success"
				else:
					return"Parking filled"
			if floor==2:
				cur = conn.cursor()
				am = conn.execute(selstring2)
				avl = am.fetchall()
				
				if avl[0][0]==None:
					conn = sqlite3.connect('itpark.db')
					conn.execute("UPDATE Plot_Tw SET id=? WHERE P_no=?",(str(id),p_no))
					conn.commit()
					return "success"
				else:
					return"Parking filled"
			if floor==3:
				cur = conn.cursor()
				am = conn.execute(selstring3)
				avl = am.fetchall()
				
				if avl[0][0]==None:
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
	return redirect('home')

@app.route('/delete',methods=['GET', 'POST'])
def delete():
	conn = sqlite3.connect('itpark.db')
	if request.method == 'GET':
		id = request.args.get('id')
		floor = request.args.get('floor')
		id = str(id)
		floor = int(floor)
		v1_list=[]

		if id not in id_list:
			return "Enter Correct ID"

		cur=conn.cursor()
		cur.execute("SELECT id FROM Plot_Fw")
		v_l=cur.fetchall()
		for x in v_l:
			v1_list.append(x[0])

		
		
		v2_list=[]
		cur.execute("SELECT id FROM Plot_Tw")
		v_l=cur.fetchall()
		for x in v_l:
			v2_list.append(x[0])
		
		

		vv_list=[]
		cur.execute("SELECT id FROM Plot_V")
		v_l=cur.fetchall()
		for x in v_l:
			vv_list.append(x[0])



		if id not in v1_list and id not in v2_list and id not in vv_list:
			return "Your vehicle is not in the Parking"

		if floor==1 and id not in v1_list:
			return "Go on the correct floor"

		if floor==2 and id not in v2_list:
			return "Go on the correct floor"

		if floor==3 and id not in vv_list:
			return "Go on the correct floor"

		if id in v1_list or id in v2_list:
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
				return " Enter Correct floor"
		else:
		 	return "Your vehicle is not in the Parking"
	return render('home')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    f = open("Message.txt", "a")
    f.write("Name = "+str(name)+"\nEmail = "+str(email)+"\nMessage = "+str(message))
    f.write("\n---------------------------------------------------------------------\n")
    f.close()
    if(check(email)):
    	return redirect('home')
    else:
    	return redirect('feedback')

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(host="0.0.0.0", port=80,debug=True)
