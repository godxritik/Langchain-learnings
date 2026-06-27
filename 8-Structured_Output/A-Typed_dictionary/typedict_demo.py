from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person : Person = {"name" : "ritik", "age" : 25}
print(new_person)

# typed dictionary will not produce any errors if data type not satisfied
new_person2 : Person = {"name" : "ritik", "age" : "25"}
print(new_person2)