import mysql.connector

var = mysql.connector.connect(password = "lalithrajr838@", host = "localhost", database = "python_practice", user = "root")

# we have to use a create a cursor to execute a queary 
cur = var.cursor()


insert_queary = """INSERT INTO students(id, name, age, grade) values(%s, %s, %s, %s)"""
insert_value  = [(1, 'lalithraj', 19, "A"),(2, 'seena', 21, "B")] 
cur.executemany(insert_queary,insert_value) # or "execute()" for single input
var.commit()  # when we perform a UPDATE DELETE and INSERT then the queary will not going to save so we have to use a " .commit() "



cur.close()
var.close()