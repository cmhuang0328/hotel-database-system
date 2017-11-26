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






db1= db.connect(host="127.0.0.1",user="root", passwd="123456")
cursor=db1.cursor()


if form.getvalue('in_date'):
in_date =' AND E.in_date='+'"'+ form.getvalue('in_date')+'"'
else:
in_date=''
if form.getvalue('out_date'):
 out_date =' AND E.out_date='+'"'+ form.getvalue('out_date')+'"'
else:
 out_date=''
if form.getvalue('pay_method'):
 pay_method=' AND E.pay_method='+'"'+ form.getvalue('pay_method')+'"'
else:
pay_method=''

temp=in_date+out_date+pay_method


sql='SELECT * FROM Final.Employee E WHERE TRUE'+temp
try:
 cursor.execute(sql)
 results=cursor.fetchall()
except:
 results="Error entered"
## actually  you will never get an error  


#print "<body>"
#print "<h2>  %s</h2>" % results
#print "</body>">"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>";
print "<title>search</title>"
print "</head>"
print "<body>"
#print "<h2> %s</h2>" % results
if results =="Error entered":
 print "<h2> %s</h2>" % results
#else:
print "<table>"
print "<tr>"
col_name_list=[tuple[0] for tuple in cursor.description]
#colnamestring=', '.join(map(str,col_name_list))
#print "<h2>{0}</h2>".format(colnamestring)
for col in col_name_list:
 print "<th>{0}</th>".format(col)
print "</tr>"
for row in results:
# mystring=', '.join(map(str,row))
# print "<h2>{0}</h2>" .format(mystring)
 print "<tr>"
 for col in row:
  print "<td>{0}</td>".format(col)
 print"</tr>"
print "</table>"
print "</body>"
print "</html>"
