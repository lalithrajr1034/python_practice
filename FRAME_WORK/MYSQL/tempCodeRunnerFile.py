# From this we will interact between sql and python 
# To install "pip install mysql-connector-python"

import mysql.connector

var1 = mysql.connector.connect(
    password='lalithrajr838@',
    host='localhost',
    user='root',
    database='python'
)
