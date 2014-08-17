import MySQLdb
import sys

class user():
	def dbConnectDetail(self):
		connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "mario", db = "login")
		return connection

	def dbLogin(self,getUser,getPass):
		connection = self.dbConnectDetail()
		cursor = connection.cursor ()
		cursor.execute ("select role from user_login where username = %s and password = %s",(getUser,getPass))
		data = cursor.fetchone ()
		cursor.close ()
		connection.close ()
		if data:
			return data[0]
		else: 
			return False
	
