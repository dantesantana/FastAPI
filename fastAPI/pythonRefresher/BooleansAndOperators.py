"""
Booleans and Operators
"""
like_coffee = True
like_tea = False
favouriteFood = "Pizza"
favouriteNumber = 32

for x in [like_tea, favouriteFood, favouriteNumber]:
    print(type(x))

# Comparison Operators
print(1 == 2)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 1)
print(1 <= 2)

# Logical Operators (and or not)
print(1 > 3 and 5 < 7)
print(1 > 3 or 5 < 7)
print(not (1 == 1))
