# coding=utf-8
import MySQLdb as db
import time;
db1= db.connect(host="127.0.0.1",user="root", passwd="123456")
cursor=db1.cursor()
sql="CREATE SCHEMA IF NOT EXISTS Final"
cursor.execute(sql)

for i in range (0,1000):
 sql = 'INSERT INTO Final.customer VALUES ('+' '+str(i)+', "'+str(i)+'", "individual",'+str(i)+', "male" , "single")'
 try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db1.commit()
 except:
    # Rollback in case there is any error
    db1.rollback()


start= time.time()


for i in range (0,100000):
 sql = """SELECT * FROM Final.customer LEFT JOIN Final.customer"""
 try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db1.commit()
 except:
    # Rollback in case there is any error
    db1.rollback()
 #time.sleep(0.01)


end= time.time()

duration=end-start
print "duration without index in left join is ",duration





sql = """ALTER TABLE Final.customer ADD INDEX 'index_c_id' ON ('c_id')"""
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()

start= time.time()

for i in range (0,100000):
 sql = """SELECT * FROM Final.customer LEFT JOIN Final.customer"""
 try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db1.commit()
 except:
    # Rollback in case there is any error
    db1.rollback()
 #time.sleep(0.01)


end= time.time()

duration=end-start
print "duration(index(c_id)) in left join is ",duration


