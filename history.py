import sqlite3


def log_gen():
	conn = sqlite3.connect('itpark.db')
	print("Opened database successfully")
	conn.execute('DROP TABLE logv')
	conn.execute('CREATE TABLE logv(id TEXT,e_name TEXT NOT NULL,v_no TEXT NOT NULL, p_lot INTEGER NOT NULL, desg TEXT NOT NULL, dep TEXT NOT NULL)')
	conn.execute('DELETE FROM logv')
	sd = conn.cursor()
	sd = conn.execute('SELECT pf.id,e.e_name,ev.V_no,P_no,e.desg,e.dep FROM Plot_Fw pf JOIN employee_vehicle ev ON e.e_id = ev.e_id JOIN employee e ON pf.id = e.e_id GROUP BY e.e_id HAVING count(*) >= 1 UNION SELECT pw.id,e.e_name,ev.V_no,P_no,e.desg,e.dep FROM Plot_Tw pw JOIN employee_vehicle ev ON e.e_id = ev.e_id JOIN employee e ON pw.id = e.e_id GROUP BY e.e_id HAVING count(*) >= 1 UNION SELECT pv.id,e.e_name,ev.V_no,P_no,e.desg,e.dep FROM Plot_V pv JOIN employee_vehicle ev ON e.e_id = ev.e_id JOIN employee e ON pv.id = e.e_id GROUP BY e.e_id HAVING count(*) >= 1' )
	am = sd.fetchall()
	conn.executemany('INSERT INTO logv VALUES(?,?,?,?,?,?);',am);
	vi = conn.execute('SELECT * FROM logv')
	vi = vi.fetchall()
	print(vi)
	conn.commit()
	return 0;

log_gen()