
import sqlite3

conn = sqlite3.connect('itpark.db')

print("Opened database successfully")


conn.execute('CREATE TABLE employee(e_id TEXT PRIMARY KEY,e_name TEXT NOT NULL, desg TEXT NOT NULL, dep TEXT NOT NULL)') 


conn.execute('CREATE TABLE type(V_no TEXT PRIMARY KEY,type INTEGER)') 

conn.execute('CREATE TABLE employee_vehicle(e_id TEXT ,v_no TEXT ,PRIMARY KEY (e_id, v_no), FOREIGN KEY(e_id) REFERENCES employee(e_id), FOREIGN KEY(v_no) REFERENCES type(v_no))') 

conn.execute('CREATE TABLE Plot_Tw(P_no INTEGER PRIMARY KEY,id TEXT)')

conn.execute('CREATE TABLE Plot_Fw(P_no INTEGER PRIMARY KEY,id TEXT)')


conn.execute('CREATE TABLE Visitor(vis_id TEXT PRIMARY KEY,v_name TEXT)')

conn.execute('CREATE TABLE meet(e_id TEXT ,vis_id TEXT,PRIMARY KEY (e_id, vis_id) FOREIGN KEY(e_id) REFERENCES employee(e_id),FOREIGN KEY(vis_id) REFERENCES employee(vis_id))')

conn.execute('CREATE TABLE Plot_V(P_no INTEGER PRIMARY KEY,id TEXT)')