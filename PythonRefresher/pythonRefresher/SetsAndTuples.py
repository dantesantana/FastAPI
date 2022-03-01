"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""
# extra 1 & 2 are ignored here!
my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
# only 5 unique elements, therefore len = 5
print(len(my_set))

for x in my_set:
    print(x)

# sets are unordered, therefore we can't print by index
# the following will error!
# print(my_set[0])

# my_set.discard(1)
# print(my_set)
# # my_set.clear()
# # print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.update([7, 8])
# print(my_set)

# Tuples are ordered like lists, but unchangable
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])
# the following will error because we can't alter tuples
# my_tuple[1] = 100

zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]
zoo.pop(3)
zoo.append("Lizard")
zoo.pop(0)
print(zoo)
print(zoo[0:3])
