# From this we will interact between sql and python 
# To install "pip install mysql-connector-python"

import mysql.connector as mydb

var1 = mydb.connect(
    password='lalithrajr838@',
    host='localhost',
    user='root',
    database='python_practice'
)

# using cursor 
cur = var1.cursor()
cur.execute("""show databases""")

for i in cur:
    print(i)
    

                                                  