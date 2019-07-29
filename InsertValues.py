import sqlite3

conn = sqlite3.connect('itpark.db')



print("Opened database successfully")

conn.execute('DELETE FROM employee_vehicle')
conn.execute('DELETE FROM employee')
conn.execute('DELETE FROM type')
conn.execute('DELETE FROM Plot_Fw')
conn.execute('DELETE FROM Plot_Tw')
conn.execute('DELETE FROM Plot_V')


conn.execute("INSERT INTO employee VALUES('TEK001','Siddhant','Associate','IT')")

conn.execute("INSERT INTO employee VALUES('TEK002','Ravi','Associate','IT')")

conn.execute("INSERT INTO employee VALUES('TEK003','Sulagna','Associate','IT')")

conn.execute("INSERT INTO employee VALUES('TEK004','Nishtha','Associate','IT')")

conn.execute("INSERT INTO employee VALUES('TEK005','Romio','Associate','IT')")

conn.execute("INSERT INTO employee VALUES('TEK006','Jyoti','Associate','IT')")

# 1 = Two Wheeler, 2 = Four Wheeler

conn.execute("INSERT INTO type VALUES('OD01T0001',1)")

conn.execute("INSERT INTO type VALUES('OD01T0009',2)")

conn.execute("INSERT INTO type VALUES('OD01T0002',1)")

conn.execute("INSERT INTO type VALUES('OD01T0010',2)")

conn.execute("INSERT INTO type VALUES('OD01T0003',1)")

conn.execute("INSERT INTO type VALUES('OD01T0004',1)")

conn.execute("INSERT INTO type VALUES('OD01T0005',1)")

conn.execute("INSERT INTO type VALUES('OD01T0006',1)")


conn.execute("INSERT INTO employee_vehicle VALUES('TEK001','OD01T0001')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK001','OD01T0009')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK002','OD01T0010')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK002','OD01T0002')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK003','OD01T0003')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK004','OD01T0004')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK005','OD01T0005')")

conn.execute("INSERT INTO employee_vehicle VALUES('TEK006','OD01T0006')")

conn.execute("INSERT INTO Plot_Fw VALUES(1,'TEK001')")
conn.execute("INSERT INTO Plot_Fw VALUES(2,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(3,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(4,'TEK002')")
conn.execute("INSERT INTO Plot_Fw VALUES(5,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(6,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(7,'TEK003')")
conn.execute("INSERT INTO Plot_Fw VALUES(8,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(9,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(10,'TEK004')")
conn.execute("INSERT INTO Plot_Fw VALUES(11,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(12,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(13,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(14,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(15,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(16,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(17,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(18,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(19,NULL)")
conn.execute("INSERT INTO Plot_Fw VALUES(20,NULL)")

conn.execute("INSERT INTO Plot_Tw VALUES(1,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(2,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(3,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(4,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(5,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(6,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(7,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(8,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(9,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(10,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(11,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(12,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(13,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(14,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(15,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(16,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(17,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(18,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(19,NULL)")
conn.execute("INSERT INTO Plot_Tw VALUES(20,NULL)")

conn.execute("INSERT INTO Plot_V VALUES(1,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(2,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(3,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(4,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(5,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(6,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(7,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(8,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(9,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(10,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(11,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(12,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(13,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(14,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(15,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(16,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(17,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(18,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(19,NULL)")
conn.execute("INSERT INTO Plot_V VALUES(20,NULL)")


conn.commit()

print("Inserted successfully")