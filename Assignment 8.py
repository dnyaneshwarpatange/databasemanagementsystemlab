import mysql.connector 
from mysql.connector import Error 
connection = mysql.connector.connect(host="localhost",user="root",password="Expert123",database="student")
try: 	
	if connection.is_connected(): 
		db_Info=connection.get_server_info()
		cursor=connection.cursor() 
		cursor.execute("insert into stud values(5,'chutiya',69);")
		cursor.execute("select * from stud")
		record=cursor.fetchall()
		print("You are connected to database: ")
		print(*record, sep="\n") 
except Error as e: 
	print("Error while connecting to MYSQL",e) 
finally: 
	if connection.is_connected(): 
		cursor.close()
		connection.close() 
		print("MYSQL connection is closed")