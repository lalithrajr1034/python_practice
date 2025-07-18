import mysql.connector

var = mysql.connector.connect(password = "lalithrajr838@", host = "localhost", database = "python_practice", user = 'root')
cur = var.cursor()

cur.execute("select * from students ")  # Executemany if there are multiple value
val = cur.fetchall()




# id=4
# name= "lalith"
# age = 46
# grade = "a"
# cur.execute(f"insert into students value({id},'{name}',{age},'{grade}')")
# var.commit()

cur.execute("select * from students;")
# Print all rows
cur.fetchone()
print(cur)
for row in cur:
    print(row)


