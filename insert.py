#!/System/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable(format='text')

import MySQLdb as db
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields

#import sys
#version = sys.version
#path = sys.path






db = MySQLdb.connect("localhost","root","123456","final" )
cursor=db1.cursor()

if form.getvalue('c_id'):
 c_id ='"'+ form.getvalue('c_id')+'"'
else:
 c_id='NULL'
if form.getvalue('c_name'):
 c_name ='"'+ form.getvalue('c_name')+'"'
else:
 c_name='NULL'
if form.getvalue('c_idtype'):
 c_idtype='"'+ form.getvalue('c_idtype')+'"'
else:
c_idtype='NULL'
if form.getvalue('c_age'):
 c_age =form.getvalue('c_age')
else:
 c_age='NULL'
if form.getvalue('c_gender'):
 c_gender ='"'+ form.getvalue('c_gender')+'"'
else:
 c_gender='NULL'
if form.getvalue('c_pref'):
 c_pref ='"'+ form.getvalue('c_pref')+'"'
else:
 c_pref='NULL'

#else:
# text_content = "Not entered"
temp= [c_id,c_name,c_idtype,c_age,c_gender,c_pref]
temp=','.join(temp)
sql1='INSERT INTO Final.customer VALUES'+"("+temp+")"
if form.getvalue('customer'):
 try:
  cursor.execute(sql1)
  db1.commit()
  result1="Insert an customer successfully"
 except:
  result1="Fail to insert an customer"
  
if form.getvalue('r_id'):
 r_id='"'+ form.getvalue('r_id')+'"'
else:
 r_id ='NULL'
if form.getvalue('c_id'):
 c_id='"'+ form.getvalue('c_id')+'"'
else:
 c_id ='NULL'
if form.getvalue('ro_id'):
 ro_id='"'+ form.getvalue('ro_id')+'"'
else:
 ro_id ='NULL'
if form.getvalue('in_date'):
 in_date='"'+ form.getvalue('in_date')+'"'
else:
 in_date ='NULL'
if form.getvalue('out_date'):
 out_date='"'+ form.getvalue('out_date')+'"'
else:
out_date ='NULL'
if form.getvalue('r_price'):
 r_price =form.getvalue('r_price')
else:
 r_price='NULL'
if form.getvalue('r_rate'):
 r_rate='"'+ form.getvalue('r_rate')+'"'
else:
 r_rate ='NULL'
if form.getvalue('no_dependents'):
 no_dependents =form.getvalue('no_dependents')
else:
 no_dependents='NULL'
if form.getvalue('pay_method'):
 pay_method =form.getvalue('pay_method')
else:
 pay_method='NULL' 


temp= [r_id,c_id,ro_id,in_date,out_date,r_price,r_rate,no_dependents,pay_method]
temp=','.join(temp)
sql2='INSERT INTO Final.reserves VALUES'+"("+temp+")"
if form.getvalue('reserves'):
 try:
  cursor.execute(sql2)
  db1.commit()
  result2="Insert a reservation successfully"
 except:
  result2="Fail to insert a reservation"


if form.getvalue('ro_id'):
 ro_id='"'+ form.getvalue('ro_id')+'"'
else:
 ro_id ='NULL'
if form.getvalue('all_discount'):
 all_discount='"'+ form.getvalue('all_discount')+'"'
else:
 all_discount ='NULL'
if form.getvalue('ro_floor'):
 ro_floor='"'+ form.getvalue('ro_floor')+'"'
else:
ro_floor ='NULL'
if form.getvalue('ro_num'):
 ro_num =form.getvalue('ro_num')
else:
 ro_num='NULL'
if form.getvalue('bed_no'):
 bed_no='"'+ form.getvalue('bed_no')+'"'
else:
 bed_no ='NULL'
if form.getvalue('bed_size'):
 bed_size =form.getvalue('bed_size')
else:
 bed_size='NULL'
if form.getvalue('max_serve'):
 max_serve =form.getvalue('max_serve')
else:
 max_serve='NULL' 


temp= [ro_id,all_discount,ro_floor,ro_num,bed_no,bed_size,max_serve]
temp=','.join(temp)
sql2='INSERT INTO Final.reserves VALUES'+"("+temp+")"
if form.getvalue('reserves'):
 try:
  cursor.execute(sql3)
  db1.commit()
  result3="Insert a room successfully"
 except:
  result3="Fail to insert a room"

#print "<body>"
#print "<h2>  %s</h2>" % results
#print "</body>">"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>";
print "<title>insert</title>"
print "</head>"
print "<body>"
if form.getvalue('customer')	
 print "<h2> %s</h2>" % result1
if form.getvalue('reserves'):
 print "<h2> %s</h2>" % result2
if form.getvalue('room'):
 print "<h2> %s</h2>" % result3
#print "<table>"
#print "<tr>"
#col_name_list=[tuple[0] for tuple in cursor.description]
#colnamestring=', '.join(map(str,col_name_list))
#print "<h2>{0}</h2>".format(colnamestring)
#for col in col_name_list:
# print "<th>{0}</th>".format(col)
#print "</tr>"
#for row in results:
# mystring=', '.join(map(str,row))
# print "<h2>{0}</h2>" .format(mystring)
# print "<tr>"
# for col in row:
#  print "<td>{0}</td>".format(col)
# print"</tr>"
#print "</table>"
print "</body>"
print "</html>"
