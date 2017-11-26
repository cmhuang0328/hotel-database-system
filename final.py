# coding=utf-8
import MySQLdb as db
db1= db.connect(host="127.0.0.1",user="root", passwd="123456")
cursor=db1.cursor()
sql="CREATE SCHEMA IF NOT EXISTS Final"
cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS Final.customer")
cursor.execute("DROP TABLE IF EXISTS Final.reserves")
cursor.execute("DROP TABLE IF EXISTS Final.room")
cursor.execute("DROP TABLE IF EXISTS Final.event")

#create table as per requirement
sql="""Create Table Final.customer(
       c_id Int(11) Not Null,
       c_name VarChar(20),
       c_idtype Enum("individual","event"),
       c_age Numeric(10),
       c_gender Enum("male","female"),
       c_pref Enum("single","double", "queen","king"),
       PRIMARY KEY (c_id) 
       );"""
#execute the sql query
cursor.execute(sql)

#create table as per requirement
sql="""Create Table Final.reserves(
        r_id Int(11) Not Null,
        c_id Int(11) Not Null,
        ro_id Int(11) Not Null,
        in_date DATE Not Null,
        out_date DATE Not Null,        
        r_price Numeric(10),
        r_rate Numeric(10),
        no_dependents Numeric(10),
        pay_method Enum("cash","credit"),
        PRIMARY KEY (r_id, c_id, ro_id) 
        );"""
#execute the sql query
cursor.execute(sql)

#create table as per requirement
sql="""Create Table Final.room(
        ro_id Int(11) Not Null,
        all_discount Enum("yes","no"),     
        ro_floor Numeric(10),
        ro_num Numeric(10),
        bed_no Numeric(10),
        bed_size Enum("single","double", "queen","king"),       
        max_serve Numeric(10),
        PRIMARY KEY (ro_id)
        );"""
#execute the sql query
cursor.execute(sql)


#create table as per requirement
sql="""Create Table Final.event(
        e_id Int(11) Not Null,
        no_participants Numeric(10),
        e_type Enum("wedding","reunion", "party"),    
        g_name VarChar(45) Not Null,  
        notes VarChar(45) Not Null,     
        PRIMARY KEY (e_id)
        );"""
#execute the sql query
cursor.execute(sql)




# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO Final.customer
         VALUES (001,"A1","event",24,"male","double"),(002,"A2","event",24,"female","double"),(003,"B1","event",24,"male","double"), (004,"B2","event",24,"male","double"), (005,"B3","event",24,"male","double"),
         (006,"C1","event",24,"male","queen"), (007,"C2","event",24,"male","queen"), (008,"C3","event",24,"male","queen"), (009,"C4","event",24,"male","queen")"""
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO Final.reserves
        VALUES (001,001,201,"2017-02-01","2017-02-03",4800,4800,1, "cash"),(001,002,201,"2017-02-01","2017-02-03",0,4800,0, "cash"),
        (002,003,202,"2017-02-01","2017-02-04", 5600,5100,2, "credit"),(002,004,202,"2017-02-01","2017-02-04", 0,5100,0, "credit"),(002,005,202,"2017-02-01","2017-02-04", 0,5100,0, "credit"),
        (003,006,301,"2017-02-01","2017-02-02",9200,8700,3, "cash"), (003,007,301,"2017-02-01","2017-02-02",0,8700,0, "cash"), (003,008,301,"2017-02-01","2017-02-02",0,8700,0, "cash"), (003,009,301,"2017-02-01","2017-02-02",0,8700,0, "cash")
        """
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO Final.room
        VALUES (201,"yes",2,1,1,"double",2), (202,"yes",2,2,2, "double", 4), (301,"yes",3,1, 2, "queen", 4)
        """
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO Final.event
        VALUES (001,2,"wedding","Jimmy's wedding", "none"), (002,3,"reunion","B's reunion", "none"), (003,4,"reunion","C's reunion", "none")
        """
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()

#Q1
print "Q1"
# Prepare SQL query to fetch records.
sql = """SELECT C.c_name FROM final.customer C, final.reserves R 
WHERE R.no_dependents>0 and R.r_rate=(SELECT MAX(r_rate) FROM reserves WHERE YEAR(out_date)=2017) and C.c_id=R.c_id"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()

   for row in results:
      c_name = row[0]
      
      # Now print fetched result
      print "c_name =", c_name

except:
   print "Error: unable to fetch data"

#Q2
print "Q2"
# Prepare SQL query to fetch records.
sql = """SELECT distinct R.ro_id FROM final.reserves R 
WHERE timestampdiff(day,in_date,out_date)=(SELECT MAX(timestampdiff(day,in_date,out_date)) FROM final.reserves) AND YEAR(R.out_date)=2017"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()

   for row in results:
      ro_id = row[0]
    
      # Now print fetched result
      print "ro_id =", ro_id

except:
   print "Error: unable to fetch data"
# disconnect from server
db1.close()
