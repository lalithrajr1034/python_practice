class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1  # increment class-level count

    @classmethod
    def total_persons(cls):
        return cls.count
p1 = Person("Lalith")
p2 = Person("Raj")

print(Person.total_persons())  # 2
