# This is a type of a funciton where function's are written in single line
"""
1. lambda funcion return hole funcion instead of returning a value
2. written in only one line
3. not used to code re-useability
4. it dosent have any name
"""


#Createing a lambda function
# ---------------------------------------
a = lambda x:x=='o'
print(a('o'))


a = lambda x: 'Even' if (x % 2) == 0 else 'Odd'
print(a(3))