import mysql.connector


try:
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='jahun2611',
        database='sakila' 
    )
    if(connection.is_connected()):
        print("successfully connected to database")
        cursor=connection.cursor()
        cursor.execute("select database();")
        dbname=cursor.fetchone()
        print("You are connected to the database: ",dbname)
        tablename="language"
        query="select * from " + tablename
        cursor.execute(query)
        tablerows=cursor.fetchall()
        for row in tablerows:
          print(row)
except mysql.connector.Error as e:
   print("error while making connection: ",e)



