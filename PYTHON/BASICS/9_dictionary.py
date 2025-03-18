# It is used store value in the form of KEY: VALUE pair

#in the dictionary we can assign a value (mortal)
la_dict={"key":"value","name":"Lalith Raj R"}
print(la_dict) 

#to manupulate a dictionary value

la_dict["raju"]="AppA" # used to add values in dictionary
la_dict["AshA"]="AmmA" # used to add values in dictionary

la_dict["name"]="Lalith" # used to change the value of same element

print(la_dict)



#............Dictionary methods.....................

dic={
    "key":"abcd",
    "name":"lalith",
    "subject" : {
        "bio":69,
        "math":87
    }
}

print(dic.keys())# we get all keys in dic -->dict_keys(['key', 'name', 'subject']) and we can write this in list form

print(dic.values())# we get all values (only values) -->dict_values(['abcd', 'lalith', {'bio': 69, 'math': 87}])

print(dic.items())# we get all key and values -->dict_items([('key', 'abcd'), ('name', 'lalith'), ('subject', {'bio': 69, 'math': 87})])

print(dic.get("name"))# we get specific key and value that we entered key name

