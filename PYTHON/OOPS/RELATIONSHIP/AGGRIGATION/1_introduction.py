# Aggrigation is a thing helps to find a relation of 'has-a' feature
#Ex: car has engine

class CustomerDetails:
    def __init__(self, name:str, gender:int, address:str):
        self.name = name
        self.gender = gender
        self.address = address

class CustomerAddress:
    def __init__(self, pin:int, village:str, state:str):
        self.pin = pin
        self.village = village
        self.state = state
        
add = CustomerAddress(571419, "Besagarahalli", "Karnataka")
details = CustomerDetails("Lalith raj R", "male", add) 

print(details.address.pin)    

# Initialising a object as a paramater to the object 