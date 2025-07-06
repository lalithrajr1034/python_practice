import mysql.connector

var = mysql.connector.connect(password = "lalithrajr838@", host = "localhost", database = "python_practice", user = 'root')
cur = var.cursor()

cur.execute("select * from students ")# Executemany if there are multiple value

