import mysql.connector

var = mysql.connector.connect(password = "lalithrajr838@", host = "localhost", database = "python_practice", user = "root")

# we have to use a create a cursor to execute a queary 
cur = var.cursor()

# #Insert a queary
# """Type 1"""
# insert_queary = """INSERT INTO students(id, name, age, grade) values(%s, %s, %s, %s)"""
# insert_value  = [(1, 'lalithraj', 19, "A"),(2, 'seena', 21, "B")] 

# cur.executemany(insert_queary,insert_value) # or "execute()" for single input

# var.commit() # when we perform a UPDATE DELETE and INSERT then the queary will not going to save so we have to use a " .commit() "


"""Type 2"""
id=4
name= "lalith"
age = 46
grade = "a"
cur.execute(f"insert into students value({id},'{name}',{age},'{grade}')")
print(cur)
var.commit()

cur.execute("select * from students;")
# Print all rows
for row in cur:
    print(row)

# Clean up
cur.close()
var.close()