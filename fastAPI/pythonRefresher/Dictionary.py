"""
Dictionaries
"""

user_dictionary = {'username': 'codingwithroby', 'name': 'eric', 'age': 32, "married": True}

print(user_dictionary)
print(len(user_dictionary))
print(user_dictionary.get("username"))

for i in user_dictionary:
    print(i)

for x, y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary
# this deletes age from user_dictionary due to the way python uses memory!
# user_dictionary2.pop("age")
# print(user_dictionary)
# we fix this by making a copy
user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
# age preserved
print(user_dictionary)
# age removed
print(user_dictionary2)

user_dictionary.clear()
print(user_dictionary)

del user_dictionary
# this line will error!
# print(user_dictionary)


my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x, y in my_vehicle.items():
    print(x, y)
vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")
print(vehicle2.keys())
for i in vehicle2:
    print(i)
