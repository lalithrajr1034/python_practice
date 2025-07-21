# single child derived from 2 or more parent 
"""
Parent1   Parent2
    \       /
      Child
    
"""

class Father:
    def skill(self):
        print("Father's skill: Gardening")

class Mother:
    def hobby(self):
        print("Mother's hobby: Painting")

class Child(Father, Mother):
    def ownSkill(self):
        print("Child's skill: Coding")



# to addingn a value to a constructor using super()

class Father:
    def __init__(self):
        print("Father constructor called")

class Mother:
    def __init__(self):
        print("Mother constructor called")
        super().__init__()  # Pass the call to next in MRO(Method Resolution Order)

class Child(Father, Mother):
    def __init__(self):
        print("Child constructor called")
        super().__init__()  # Automatically calls Father -> Mother (MRO order)

obj = Child()
