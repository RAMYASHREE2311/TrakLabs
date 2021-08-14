import mysql.connector
import falcon
import json
class Management():
	def on_get(self,req,resp):
		mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="managementsystem")
		mycursor=mydb.cursor()
        mycursor.execute(req)
		for i in mycursor:
			a = json.dumps(i)
	    resp.body = a
	    resp.status = falcon.HTTP_OK
    
 